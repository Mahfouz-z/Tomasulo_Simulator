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



    def branch (self, operand1, operand2, offset,  pc):
        self.counter= self.maxCounter
        self.offset = offset
        self.PC=pc
        if operand1 == operand2: 
            self.pc= offset
            self.taken = True 
        else:
            self.pc= pc + 1
            self.taken = False
        self.result= self.pc

    def count(self):
        self.counter-=1
        
   
    def missPridected(self):
        return (self.taken and (self.offset > self.PC)) or ((not self.taken) and (self.offset < self.PC))

    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None