
class insrtuctionUnit:
    def __init__ (self, line):
        f=open(line)
        self.instructions=f.read()
        f.close()
        self.instructions=self.instructions.split('\n')
        self.instructionList=[]
        for q in self.instructions:
            q=instruction(q)
            self.instructionList.append(q)
        self.issueList=[]
        
    def getIssue(self, n):
        issue=[]
        while (n>0):
            self.issueList.append(self.instructionList.pop(0))
            n-=1
        issue=self.issueList
        return issue
    def revIssue(self, n):
        self.issueList.reverse()
        while(n>0):
            self.instructionList.insert(0, self.issueList.pop(0))
            n-=1
            
    
class instruction:
    def __init__ (self, inst):
        self.temp=inst.replace(',', '')
        self.temp= self.temp.replace('(', '')
        self.temp= self.temp.replace(')', '')
        self.temp= self.temp.split(" ")
        self.instType=self.temp[0]
        self.r1=self.temp[1]
        self.r2=self.temp[2]
        self.imm=self.temp[2]
        self.r3=self.temp[3]
        
        
 
    
            
        
        


