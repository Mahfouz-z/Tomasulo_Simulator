class Adders: 
    def __init__(self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.op = ""
       self.maxCounter = counter
       self.counter = -1 

    def operation(self, index, operand1, operand2, op, counter):
        self.counter = self.maxCounter
        self.index = index
        if op =="add": 
            self.result = operand1+ operand2
        elif op =="sub":
            self.result = operand1 - operand2 
        elif op == "addi":
            self.result = operand1+ operand2
        else : 
            self.result= 0
        
    def count(self):
        self.counter-=1
        
    def ready(self):   
        if(self.counter == 0):
            return self.result, self.index
        else:
            return None 
        