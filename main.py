from DataMemClass import dataMem
from robClass import ROB
from instructionUnit  import insrtuctionUnit


assmFilePath = input("Please enter assembly file path:")
dataMemInitFilePath = input("Please input data memorey init file path:")

dataMem0 = dataMem(dataMemInitFilePath)
instQueue0 = insrtuctionUnit(assmFilePath)
ROB0 = ROB(8)
RS0 = RS() 

clk = 0
inst_addr = 0
numberOfIssues = 2
while True:
    for i in range(numberOfIssues):
        issue = instQueue0.getIssue(1, inst_addr)
        instType = issue[0].instType
        if(RS0.checkAvailable(instType)):
            if(ROB0.check_available() >= 1):
                


     
