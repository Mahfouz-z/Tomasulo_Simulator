class BEQ: 
    def __init__(self,  counter):
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.counter = counter
       self.maxCounter = counter
       self.pc= 0
       self.index = 0
       self.taken = False
       self.result=0



    def branch (self, operand1, operand2,  pc, offset):
        self.counter= self.maxCounter
        if operand1 == operand2: 
            self.pc= offset
            self.taken = True 
        else:
            self.pc= pc + 1
            self.taken = False
        self.result= self.pc

    def count(self):
        self.counter-=1
        
   
    def getTaken(self):
        return self.taken

    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None