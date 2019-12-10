from DataMemClass import dataMem
from robClass import ROB
from instructionUnit  import insrtuctionUnit
from RegFile import RegFile
from RS_Class import RS


#assmFilePath = input("Please enter assembly file path:")
#dataMemInitFilePath = input("Please input data memorey init file path:")

#dataMem0 = dataMem(dataMemInitFilePath)
#instQueue0 = insrtuctionUnit(assmFilePath)
instQueue0 = insrtuctionUnit("inst.txt")
config={}
config["lw_num"]=2
config["sw_num"]=2
config["jmp_num"]=2
config["beq_num"]=2
config["add_num"]=2
config["nand_num"]=2
config["mult_num"]=2


ROB0 = ROB()
RS0 = RS(config) 
reg={}
for i in range(8):
    reg["x"+ str(i)]=RegFile(None, 0)
clk = 0
pc = 0
numberOfIssues = 2



while True:
    for i in range(numberOfIssues):
        issue = instQueue0.getIssue(1, pc)
        instType = issue[0].instType
        if(RS0.checkAvailable(instType)):
            if(ROB0.check_available() >= 1):
                RS0.issue(instType, reg[issue[0].r2], reg[issue[0].r3], reg[issue[0].r2].ROBNumber, reg[issue[0].r3].ROBNumber )
                ROB0.initiate_entry(issue[0])
            else:
                break     
        else:
            break


     
