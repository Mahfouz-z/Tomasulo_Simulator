class LW: 
    def __init__ (self, counter):
        self.state = True
        self.operand1= 0
        self.offset= 0
        self.address= 0
        self.destination = 0
        self.index= 0
        self.maxCounter = counter
        self.counter = counter
        self.result = 0

    def getAddress (self, operand1, offset, index):
        self.address = operand1 + offset
        self.index = index
        return self.address

    def load (self, destinationIn):
        self.destination= destinationIn
        self.result = self.destination

    def getIndex(self):
        return self.index
        
    def count(self):
        self.counter -= 1

    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None