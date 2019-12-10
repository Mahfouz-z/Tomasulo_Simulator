
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
        
    def getIssue(self, n, addr):
        issue=[]
        i=0
        while (i<n):
            issue.append(self.instructionList[addr+i])
            i+=1
        self.issueList=issue
        return issue
    def revIssue(self, n, addr):
        self.issueList.reverse()
        while(n>0):
            self.issueList.pop(0)
            n-=1
            
    
class instruction:
    def __init__ (self, inst):
        self.temp=inst.replace(',', '')
        self.temp= self.temp.replace('(', '')
        self.temp= self.temp.replace(')', '')
        self.temp= self.temp.split(" ")
        self.instType=self.temp[0]
        self.r1=self.temp[1]
        if(self.temp[2][0]=='x'):
            self.r2=self.temp[2]
        else:
            self.r2='x0'
        if(self.temp[2][0]!='x'):
            self.imm=int(self.temp[2])
        else:
            self.imm=0
        self.r3=self.temp[3]
        
        
 
    
            
        
        


