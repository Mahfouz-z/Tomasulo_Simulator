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
        return (self.taken and self.offset > 0) or ((not self.taken) and self.offset < 0)

    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None