class NAND: 
    def __init__(self, counter):
       self.result = 0
       self.operand1 = 0 
       self.operand2= 0
       self.state = True
       self.counter =counter
       self.maxCounter = counter


    def Nand(self, operand1, operand2):
        self.counter = self.maxCounter
        self.result = not (operand1 and operand2)
        

    def count(self):
        self.counter-=1
        
    def ready(self):   
        if(self.counter == 0):
            return self.result
        else:
            return None 

        