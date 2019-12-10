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
                buffer_entry["Ready"] = "No"
                self.buffer.append(buffer_entry)


        def check_available(self):
            return self.available 

        def initiate_entry(self, inst):
            self.buffer[self.tail]["Type"] = get_inst_type(inst)
            self.buffer[self.tail]["Dest"] = get_inst_dest(inst)
            self.buffer[self.tail]["Value"] = "unkown"
            self.tail += 1
