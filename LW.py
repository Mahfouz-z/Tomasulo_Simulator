class LW: 
    def __init__ (self, counter):
        self.state = True
        self.counter= counter
        self.operand1= 0
        self.offset= 0
        self.address= 0
        self.destination = 0

    def getAddress (self, operand1, offset):
        self.address = operand1 + offset
        return self.address

    def load (self, destinationIn):
        self.destination= destinationIn
        return self.destination

    def count(self:
        self.counter-=1
        return self.counter 