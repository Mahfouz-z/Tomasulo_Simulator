from DataMemClass import dataMem
from robClass import ROB
from instructionUnit  import *
from RegFile import RegFile
from RS_Class import RS
from NAND import NAND
#from Multipliers import *
#from Multipliers import *
#from Adders import *
#from BEQ import *
#from JMP import *
#from LW import *
#from SW import *


#assmFilePath = input("Please enter assembly file path:")
#dataMemInitFilePath = input("Please input data memorey init file path:")

dataMem0 = dataMem("dataMem.txt")#dataMemInitFilePath)
#instQueue0 = insrtuctionUnit(assmFilePath)

############# Read the Configration file ############
f = open ("fu.txt", 'r')
fuInfo = f.read()
f.close()
fuInfo = fuInfo.split("\n")
c=0
for line in fuInfo:
    fuInfo[c]=line.split(" ")
    c+=1
di={}
for i in fuInfo:
    di[i[0]]= int(i[1]),int(i[2])
####################################################

instQueue0 = insrtuctionUnit("test.txt")
lastPC=instQueue0.lastPC()
config={} #TODO take it from a file
config = di 


ROB0 = ROB()
RS0 = RS(config) 
beqNum = 0
beqMissPredicted = 0
missPredicted = False

# reg_file
reg={}
for i in range(8):
    reg["x"+ str(i)]=RegFile(None, i)

ebreak = False
clk = 0
pc = 0
nextPC = []
nextPCJ = []
wordAdd = 0
numberOfIssues = 2
stationsNumber = RS0.station_num_total()

com=0
#### We better add the immediate calculation of the load and store to the reservation station class and make it part of the RS to be ready 

while (clk<100):
    #simulation commit 
    
    for i in range (numberOfIssues):
        commit=ROB0.checkHead()
        if(commit == "ebreak"):
            ebreak = True
        elif(commit!=None):
            com+=1
            robType=commit["Type"]
            if(robType=="add" or robType=="addi" or robType== "sub" or robType=="nand" or robType=="mult"):
                rd=commit["Dest"]
                reg[rd].data=commit["Value"]
                if(robType=="add" or robType=="addi" or robType== "sub"):
                    if(reg[rd].ROBNumber==ROB0.head):
                        reg[rd].ROBNumber= -1
                else: reg[rd].ROBNumber= -1
                ROB0.remove_entry()
            elif(robType=="beq"):
                beqNum += 1
                if missPredicted:
                    pc = nextPC[0]
                    nextPC = []
                    ROB0.flush()
                    RS0.flush()
                    for r in range(8):
                       reg["x"+ str(r)].flush()
                    missPredicted = False
                ROB0.remove_entry()
            elif(robType == "jmp" or robType == "jalr" or robType == "ret"):
                pc = nextPCJ[0]
                nextPCJ = []
                ROB0.flush()
                RS0.flush()
                for r in range(8):
                    reg["x"+ str(r)].flush()
            elif robType == "lw": 
                rd=commit["Dest"]
                reg[rd].data=commit["Value"]
                reg[rd].ROBNumber=-1
                ROB0.remove_entry()
            elif robType == "sw":
                dataMem0.update(wordAdd, commit["Value"])
                ROB0.remove_entry()
            #elif robType == "ebreak":
                
    
    if ebreak:
        break

    #simulating execute and writing stage
    for i in range(stationsNumber):
        if(RS0.get_status(i) == "executing"):
            result = RS0.decFuncUnitCount(i)
        if(RS0.get_status(i) == "done"):
            robIndex = RS0.getTargetRob(i)
            instType = RS0.get_type(i)
            if (instType == "jmp" or instType == "jalr" or instType == "ret"): #TODO jalr doesn't write to a register
                nextPCJ.append(result)
                ROB0.upd_entry(robIndex,result)
            elif instType == "beq":
                beqNum += 1
                if RS0.get_missPridected():
                    nextPC.append(result)
                    beqMissPredicted += 1
                    missPredicted = True
                ROB0.upd_entry(robIndex,result)
            elif instType == "lw":
                wordAdd = result
                ROB0.upd_entry(robIndex,dataMem0.getData(wordAdd))
            elif instType == "sw":
                wordADD = result
                ROB0.upd_entry(robIndex,RS0.get_Vj(i))
            elif instType == "ebreak":
                pass
            else:
                ROB0.upd_entry(robIndex,result)

            RS0.updRS(robIndex,result)
            RS0.write(i)
        if(RS0.ready(i)):
            RS0.execute(i, pc)

    #resultE = RS0.decFuncUnitCount(RS0.station_num_total())
    #if(resultE == "ebreak"):
    #    robIndex = RS0.getTargetRob(RS0.station_num_total())
    #    instType = RS0.get_type(RS0.station_num_total())
    #    ROB0.upd_entry(robIndex,resultE)
    #RS0.execute(RS0.station_num_total(), pc)
    
    #simulating issue stage
    for i in range(numberOfIssues):
        if(pc<=lastPC):
            issue = instQueue0.getIssue(1, pc)
            instType = issue[0].instType
            if(RS0.available(instType)):
                if(ROB0.check_available() >= 1):
                    dest=ROB0.initiate_entry(issue[0])
                    RS0.issue(instType, reg[issue[0].r2].data, reg[issue[0].r3].data, reg[issue[0].r2].ROBNumber, reg[issue[0].r3].ROBNumber, dest, int(issue[0].imm))
                    reg[issue[0].r1].ROBNumber=dest
                    if(instType == 'beq'):
                        if(int(issue[0].imm)<=pc):
                            pc=int(issue[0].imm)
                        else:
                            pc+=1
                    else:    
                        pc+=1
                else:
                    break     
            else:
                break
    
    clk+=1


print("The time of excution is:" + str(clk) + "cycles")
print("The IPC is:" + str(com / clk))
print ("the ratio of branch mispredictions is:" + str(beqMissPredicted/beqNum))
