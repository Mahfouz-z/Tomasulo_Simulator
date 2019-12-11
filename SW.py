class SW: 
    def __init__ (self, counter):
        self.state = True
        self.counter = counter
        self.maxCounter = counter
        self.operand1 = 0
        self.offset = 0
        self.address = 0
        self.result = 0
        
        

    def getAddress (self, operand1, offset, index):
        self.counter = self.maxCounter
        self.address = operand1 + offset
        self.index = index
        self.result = self.address

    def getIndex(self):
        return self.index

    def count(self):
        self.counter-=1
    
    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None