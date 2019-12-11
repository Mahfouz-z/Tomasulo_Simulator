def get_inst_type(inst):
    div_inst = inst.split(" ")
    return div_inst[0]

def get_inst_dest(inst):
    div_inst = inst.split(" ")
    div_inst = div_inst[1].split(",")
    return div_inst[0]

class ROB:
        def __init__(self):
            self.head = 0
            self.tail = 0
            self.available = 8
            self.buffer = []
            for i in range(8):
                buffer_entry = {}
                buffer_entry["Type"] = "init"
                buffer_entry["Dest"] = "init"
                buffer_entry["Value"] = "init"
                buffer_entry["Ready"] = False
                self.buffer.append(buffer_entry)


        def check_available(self):
            return self.available 

        def initiate_entry(self, inst):
            self.buffer[self.tail]["Type"] = inst.instType
            self.buffer[self.tail]["Dest"] = inst.r1
            self.buffer[self.tail]["Value"] = "unkown"
            self.tail = (self.tail+1)%8
            self.available-=1
            return (self.tail-1)
        def remove_entry(self):
            self.buffer[self.head]["Type"] = "init"
            self.buffer[self.head]["Dest"] = "init"
            self.buffer[self.head]["Value"] = "init"
            self.buffer[self.head]["Ready"] = False
            self.head = (self.head+1)%8
            self.available+=1
            
        def upd_entry(self, index, res):
            self.buffer[index]["Value"]=res
            self.buffer[index]["Ready"]=True
        def checkHead(self):
            if(self.buffer[self.head]["Ready"]):
                return self.buffer[self.head]
            else: return None
            
            
       
