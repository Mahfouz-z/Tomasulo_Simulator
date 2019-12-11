class Multipliers:

    def __init__(self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.counter = counter
       self.index = 0  

    def mul(self, result, operand1, operand2,index):
        self.result = operand1 * operand2
        self.index = index
        return result

    def getIndex(self):
        return self.index
        
    def count(self):
        self.counter-=1
        return self.counter
        