class LW: 
    def __init__ (self, counter):
        self.operand1= 0
        self.offset= 0
        self.address= 0
        self.maxCounter = counter+1
        self.counter = counter+1
        self.result = 0

    def getAddress (self, operand1, offset):
        self.counter = self.maxCounter
        self.address = operand1 + offset
        self.result = self.address

        
    def count(self):
        self.counter -= 1

    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None
