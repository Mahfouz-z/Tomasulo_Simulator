class BEQ: 
    def __init__(self,  counter,):
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.counter =counter
       self.pc= 0
       self.offset= 0


    def branch (self, operand1, operand2,  pc, offset):
        if operand1 == operand2: 
            self.pc= pc + offset 
        else:
            self.pc= pc + 4

        return pc

    def count(self):
        self.counter-=1
        return self.counter
        

    def getPC(self, pcIn):
        self.pc = pcIn

    def getOffset(self, offsetIn):
        self.offset = offsetIn
