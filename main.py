from DataMemClass import dataMem
from robClass import ROB
from instructionUnit  import insrtuctionUnit


assmFilePath = input("Please enter assembly file path:")
dataMemInitFilePath = input("Please input data memorey init file path:")

dataMem0 = dataMem(dataMemInitFilePath)
instQueue0 = insrtuctionUnit(assmFilePath)
ROB = ROB(8)

while True:
     
