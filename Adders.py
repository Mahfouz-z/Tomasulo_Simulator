class Adders: 
    def __init__(self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.op = ""
       self.counter = counter
       self.maxCounter = counter
       self.index = 0

    def operation(self, operand1, operand2, op):
        self.counter = self.maxCounter
        if op =="add": 
            self.result = operand1 + operand2
        elif op =="sub":
            self.result = operand1 - operand2 
        elif op == "addi":
            self.result = operand1 + operand2
        else : 
            self.result = 0
         
        
    def count(self):
        self.counter -= 1
        
    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None