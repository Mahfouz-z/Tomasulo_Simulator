class JMP: 
    def __init__(self,  counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.op = ""
       self.counter =counter
       self.pc= 0
       self.address= 0


    def operation(self, result, operand1, operand2, address, op, pc):

        if op =="jalr": 
            self.result =  pc + 4
            self.address = (operand1 + operand2) & -2

        elif op =="jmp": 
            self.address= operand1 + pc

        elif op == "ret":
            self.address = (operand1 + operand2) & -2
        else : 
            self.result= 0
            self.address = 0
        
        
        return result, address 

   def count(self):
        self.counter-=1
        return self.counter
       

    def getPC(self, pcIn):
        self.pc = pcIn
