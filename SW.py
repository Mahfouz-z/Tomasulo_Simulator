class SW: 
    def __init__ (self, counter):
        self.state = True
        self.counter= counter
        self.operand1= 0
        self.offset= 0
        self.address= 0
        

    def getAddress (self, operand1, offset, index):
        self.address = operand1 + offset
        self.index = index
        return self.address

    def getIndex(self):
        return self.index
        
    def count(self):
        self.counter-=1
        return self.counter