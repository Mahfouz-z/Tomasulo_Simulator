from DataMemClass import dataMem
from robClass import ROB
from instructionUnit  import *
from RegFile import RegFile
from RS_Class import RS
from Multipliers import *
from NAND import NAND
from Multipliers import *
from Adders import *
from BEQ import *
from JMP import *
from LW import *
from SW import *

#assmFilePath = input("Please enter assembly file path:")
#dataMemInitFilePath = input("Please input data memorey init file path:")

#dataMem0 = dataMem(dataMemInitFilePath)
#instQueue0 = insrtuctionUnit(assmFilePath)

instQueue0 = insrtuctionUnit("inst.txt")
config={}
config["lw"]=2
config["sw"]=2
config["jmp"]=2
config["beq"]=2
config["add"]=2
config["nand"]=2
config["mult"]=2


ROB0 = ROB()
RS0 = RS(config) 

mul0=Multipliers(2)
add0 = Adders(2)
nand0= NAND(1)
lw0 = LW(3)
sw0=SW(3)
jmp0= JMP(1)
beq0=BEQ(1)


# reg_file
reg={}
for i in range(8):
    reg["x"+ str(i)]=RegFile(None, 0)

reg['x2'].data=5
clk = 0
pc = 0

numberOfIssues = 2
stationsNumber = RS0.station_num_total()



while (clk<6):

    #simulating execute stage

    for i in range(stationsNumber):
        if(RS0.ready(i)):
            RS0.execute(i)
            oper=RS0.station[i]["op"]
            if(oper == 'add' or oper =='sub'or oper=='addi'):
                add0.operation(RS0.station[i]["Vj"],RS0.station[i]["Vk"], RS0.station[i]["op"], i)
            if(oper == 'mult'):
                mul0.mul(RS0.station[i]["Vj"],RS0.station[i]["Vk"], i)
            if(oper =='nand'):
                nand0.Nand(RS0.station[i]["Vj"],RS0.station[i]["Vk"], i)
            if(oper == 'lw'):
                lw0.getAddress(RS0.station[i]["Vj"],RS0.station[i]["Vk"], RS0.station[i]["op"], i)
            if(oper == 'sw'):
                sw0.getAddress(RS0.station[i]["Vj"],RS0.station[i]["Vk"], RS0.station[i]["op"], i)
            if(oper == 'jmp' or oper =='jalr'or oper =='ret'):
                jmp0.operation(RS0.station[i]["Vj"],RS0.station[i]["Vk"], RS0.station[i]["op"], pc, i)
            if(oper == 'beq'):
                beq0.branch(RS0.station[i]["Vj"],RS0.station[i]["Vk"], pc, RS0.station[i]["A"], i)
                
            
            
    
    
    #simulating issue stage
    for i in range(numberOfIssues):
        issue = instQueue0.getIssue(1, pc)
        instType = issue[0].instType
        if(RS0.available(instType)):
            if(ROB0.check_available() >= 1):
                dest=ROB0.initiate_entry(issue[0])
                RS0.issue(instType, reg[issue[0].r2].data, reg[issue[0].r3].data, reg[issue[0].r2].ROBNumber, reg[issue[0].r3].ROBNumber, dest, reg[issue[0].r3].data+int(issue[0].imm))
                if(instType == 'beq'):
                    if(int(issue[0].imm)<0):
                        pc=pc+int(issue[0].imm)
                    else:
                        pc+=1
                else:    
                    pc+=1
            else:
                break     
        else:
            break
    
    
    clk+=1         
