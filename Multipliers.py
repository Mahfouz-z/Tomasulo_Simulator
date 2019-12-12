class Multipliers:
    def __init__ (self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.counter = counter
       self.maxCounter = counter
       self.index = 0  

    def mul(self, operand1, operand2):
        self.counter = self.maxCounter
        self.result = operand1 * operand2

        
    def count(self):
        self.counter -= 1

    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None

