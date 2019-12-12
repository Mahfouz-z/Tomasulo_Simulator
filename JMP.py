class JMP: 
    def __init__(self,  counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.op = ""
       self.counter = counter
       self.maxCounter = counter
       self.pc= 0
       self.address= 0
       self.index=0 


    def operation(self, operand1, operand2, op, pc):
        self.counter= self.maxCounter
        if op == "jalr": 
            self.result =  pc + 4
            self.address = (operand1 + operand2) & -2

        elif op =="jmp": 
            self.address= operand1 + pc
            self.result = 0
        elif op == "ret":
            self.address = (operand1 + operand2) & -2
            self.result = 0
        else : 
            self.result= 0
            self.address = 0
        
    def count(self):
        self.counter-=1
       
    def getIndex(self):
        return self.index

    def getAddress(self):
        return self.address

    def ready(self):   
        if(self.counter == 0):
            return self.address
        else:
            return None