class NAND: 
    def __init__(self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.counter =counter


    def Nand(self, result, operand1, operand2, index):
        self.result = not (operand1 and operand2)
        self.index= index
        return self.result

    def getIndex(self):
        return self.index

    def count(self):
        self.counter-=1
        return self.counter
        