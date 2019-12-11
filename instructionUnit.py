
class insrtuctionUnit:
    def __init__ (self, line):
        f=open(line)
        self.instructions=f.read()
        f.close()
        self.instructions=self.instructions.split('\n')
        self.instructionList=[]
        self.labeldict={}
        for q in self.instructions:
            if(q[len(q)-1]==':'):
                q=q.replace(':', '')
                self.labeldict[q]=self.instructions.index(q+':')
        for q in self.instructions:
            if(q[len(q)-1]!=':'):
                q=instruction(q)
                if(q.imm.isdigit()!=1):
                    q.imm=self.labeldict[q.imm]+1
                else: q.imm=int(q.imm)
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
            
    def lastPC(self):
        return len(self.instructionList)-1
        
class instruction:
    def __init__ (self, inst):
        self.temp=inst.replace(',', '')
        self.temp= self.temp.replace('(', '')
        self.temp= self.temp.replace(')', '')
        self.temp= self.temp.split(" ")
        self.instType=self.temp[0]
        if(self.instType!= "jmp" and self.instType!= "addi" and self.instType!= "beq" and self.instType!= "ret" and self.instType!= "jalr" ):
            self.r1=self.temp[1]
            if(self.temp[2][0]=='x'):
                self.r2=self.temp[2]
            else:
                self.r2='x0'
            if(self.temp[2][0]!='x'):
                self.imm=self.temp[2]
            else:
                self.imm='0'
            self.r3=self.temp[3]
        elif(self.instType== "ret"):
            self.r1='x0'
            self.r2='x0'
            self.r3='x0'
            self.imm='0'
        elif(self.instType== "beq"):
            self.r2=self.temp[1]
            self.r3=self.temp[2]
            self.imm=self.temp[3]
            self.r1='x0'
        elif(self.instType== "jmp"):
            self.r2='x0'
            self.r3='x0'
            self.imm=self.temp[1]
            self.r1='x0'
        elif(self.instType== "jalr"):
            self.r1='x1'
            self.r2=self.temp[1]
            self.r3='x0'
            self.imm='0'
        elif(self.instType== "addi"):
            self.r1=self.temp[1]
            self.r2=self.temp[2]
            self.r3='x0'
            self.imm=self.temp[3]
        
 
    
            
        
        


