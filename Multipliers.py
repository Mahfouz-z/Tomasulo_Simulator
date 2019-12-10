class Multipliers:

    def __init__(self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.counter = counter  

    def mul(self, result, operand1, operand2):
        self.result = operand1 * operand2
        return result

    def count(self):
        self.counter-=1
        return self.counter
        