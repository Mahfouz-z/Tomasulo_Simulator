class Multipliers:

   def __init__(self, result, operand1, operand2, state, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.counter = 0  

    def mul(self, result, operand1, operand2):
        self.result = self.operand1 * self.operand2
        return self.result
         
    def count(self,counter):
        self.counter+=1
        return counter 
