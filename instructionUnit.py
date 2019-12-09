
class insrtuctionUnit:
    def __init__ (self, line):
        f=open(line)
        self.instructionList=f.read()
        f.close()
        self.instructionList=self.instructionList.split('\n')
        self.issueList=[]
        
    def getIssue(self, n):
        while (n>0):
            self.issueList.append(self.instructionList.pop(0))
            n-=1
        return self.issueList
    def revIssue(self, n):
        while(n>0):
            self.instructionList.insert(1, self.issueList.pop(0))
            
            
    
    
    
            
        
        

line = "inst.txt"
listt = insrtuctionUnit(line)
i=listt.getIssue(2)
#listt.revIssue(1)