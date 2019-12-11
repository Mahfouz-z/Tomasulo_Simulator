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
config["add"]=3
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


#### We better add the immediate calculation of the load and store to the reservation station class and make it part of the RS to be ready 

while (clk<3):

    #simulating execute stage

    for i in range(stationsNumber):
        if(RS0.get_status(i) == "executing"):
            result = RS0.decFuncUnitCount(i)
        if(RS0.get_status(i) == "done"):
            cdbData = {}
            cdbData["result"] = result
            cdbData["targetRob"] = RS0.getTargetRob(i) 
            RS0.write(i)
        if(RS0.ready(i)):
            RS0.execute(i, pc)

    
    #simulating issue stage
    for i in range(numberOfIssues):
        issue = instQueue0.getIssue(1, pc)
        instType = issue[0].instType
        if(RS0.available(instType)):
            if(ROB0.check_available() >= 1):
                dest=ROB0.initiate_entry(issue[0])
                RS0.issue(instType, reg[issue[0].r2].data, reg[issue[0].r3].data, reg[issue[0].r2].ROBNumber, reg[issue[0].r3].ROBNumber, dest, int(issue[0].imm))
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
