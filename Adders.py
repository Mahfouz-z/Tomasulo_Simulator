class Adders: 
    def __init__(self,  counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.op = ""
       self.counter =counter
       self.index = 0

    def operation(self, result, operand1, operand2, op, index):
        if op =="add": 
            self.result = operand1+ operand2
        elif op =="sub":
            self.result = operand1 - operand2 
        elif op == "addi":
            self.result = operand1+ operand2
        else : 
            self.result= 0
        self.index = index
        return result
         
    def getIndex(self):
        return self.index

    def count(self):
        self.counter-=1
        return self.counter
        