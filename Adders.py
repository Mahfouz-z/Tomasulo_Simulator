class Adders: 
    def __init__(self,  counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.op = ""
       self.counter =counter

    def operation(self, result, operand1, operand2, op):
        if op =="add": 
            self.result = operand1+ operand2
        elif op =="sub":
            self.result = operand1 - operand2 
        elif op == "addi":
            self.result = operand1+ operand2
        else : 
            self.result= 0
        return result

    def count(self):
        self.counter-=1
        return self.counter
        