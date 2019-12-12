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

#dataMem0 = dataMem(dataMemInitFilePath)
#instQueue0 = insrtuctionUnit(assmFilePath)

instQueue0 = insrtuctionUnit("test.txt")
lastPC=instQueue0.lastPC()
config={}
config["lw"]=2
config["sw"]=2
config["jmp"]=2
config["beq"]=2
config["add"]=3
config["nand"]=2
config["mult"]=2


ROB0 = ROB()
RS0 = RS(config) 
beqNum = 0
beqMissPredicted = 0
missPredicted = False

# reg_file
reg={}
for i in range(8):
    reg["x"+ str(i)]=RegFile(None, 0)

reg['x2'].data=7
clk = 0
pc = 0
nextPC = []
nextPCJ = []

numberOfIssues = 2
stationsNumber = RS0.station_num_total()


#### We better add the immediate calculation of the load and store to the reservation station class and make it part of the RS to be ready 

while (clk<9):

    #simulation commit stage
    for i in range (numberOfIssues):
        commit=ROB0.checkHead()
        if(commit!=None):
            robType=commit["Type"]
            if(robType=="add" or robType=="addi" or robType== "sub" or robType=="nand" or robType=="mult"):
                rd=commit["Dest"]
                reg[rd].data=commit["Value"]
                reg[rd].ROBNumber=-1
                ROB0.remove_entry()
            elif(robType=="beq"):
                if missPredicted:
                    pc = nextPC[0]
                    nextPC = []
                    ROB0.flush()
                    missPredicted = False
                ROB0.remove_entry()
            elif(robType == "jmp" or robType == "jalr" or robType == "ret"):
                pc = nextPCJ[0]
                nextPCJ = []
                ROB0.flush()
            
    
    #simulating execute and writing stage
    for i in range(stationsNumber):
        if(RS0.get_status(i) == "executing"):
            result = RS0.decFuncUnitCount(i)
        if(RS0.get_status(i) == "done"):
            robIndex = RS0.getTargetRob(i)
            instType = RS0.get_type(i)
            if (instType == "jmp" or instType == "jalr" or instType == "ret"):
                nextPCJ.append(result)
            if instType == "beq":
                beqNum += 1
                if RS0.get_missPridected():
                    nextPC.append(result)
                    beqMissPredicted += 1
                    missPredicted = True
            ROB0.upd_entry(robIndex,result)
            RS0.updRS(robIndex,result)
            RS0.write(i)
        if(RS0.ready(i)):
            RS0.execute(i, pc)

    
    #simulating issue stage
    for i in range(numberOfIssues):
        if(pc<=lastPC):
            issue = instQueue0.getIssue(1, pc)
            instType = issue[0].instType
            if(RS0.available(instType)):
                if(ROB0.check_available() >= 1):
                    dest=ROB0.initiate_entry(issue[0])
                    reg[issue[0].r1].ROBNumber=dest
                    RS0.issue(instType, reg[issue[0].r2].data, reg[issue[0].r3].data, reg[issue[0].r2].ROBNumber, reg[issue[0].r3].ROBNumber, dest, int(issue[0].imm))
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
