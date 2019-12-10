from DataMemClass import dataMem
from robClass import ROB
from instructionUnit  import insrtuctionUnit
from RegFile import RegFile


assmFilePath = input("Please enter assembly file path:")
dataMemInitFilePath = input("Please input data memorey init file path:")

dataMem0 = dataMem(dataMemInitFilePath)
instQueue0 = insrtuctionUnit(assmFilePath)
ROB0 = ROB(8)
RS0 = RS() 
regFile={}
for i in range(8):
    regFile["x", str(i)]=RegFile(None, 0)
clk = 0
pc = 0
numberOfIssues = 2



while True:
    for i in range(numberOfIssues):
        issue = instQueue0.getIssue(1, pc)
        instType = issue[0].instType
        if(RS0.checkAvailable(instType)):
            if(ROB0.check_available() >= 1):
                if():
                    RS0.issue(instType, reg[issue[0].r2], reg[issue[0].r3], regStatus )

                ROB0.initiate_entry(issue[0])
            else:
                break     
        else:
            break


     
