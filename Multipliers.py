class Multipliers:

    def __init__(self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.maxCounter = counter  
       self.counter = -1

    def mul(self, index, operand1, operand2):
        self.counter = self.maxCounter
        self.index = index
        self.result = operand1 * operand2
        
    def count(self):
        self.counter-=1

    def ready(self):   
        if(self.counter == 0):
            return self.result, self.index
        else:
            return None 