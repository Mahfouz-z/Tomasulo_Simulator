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
config["lw"]=2
config["sw"]=2
config["jmp"]=2
config["beq"]=2
config["add"]=2
config["nand"]=2
config["mult"]=2


ROB0 = ROB()
RS0 = RS(config) 
reg={}
for i in range(8):
    reg["x"+ str(i)]=RegFile(None, 0)
clk = 0
pc = 0
numberOfIssues = 4



#while True:
for i in range(numberOfIssues):
    issue = instQueue0.getIssue(1, pc)
    instType = issue[0].instType
    if(RS0.available(instType)):
        if(ROB0.check_available() >= 1):
            dest=ROB0.initiate_entry(issue[0])
            RS0.issue(instType, reg[issue[0].r2].data, reg[issue[0].r3].data, reg[issue[0].r2].ROBNumber, reg[issue[0].r3].ROBNumber, dest, reg[issue[0].r3].data+int(issue[0].imm)  )
            pc+=1
        else:
            break     
    else:
        break


     
