def get_inst_type(inst):
    div_inst = inst.split(" ")
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

        def initiate_entries(self, first_inst, second_inst):
            self.buffer[self.tail]["Type"] = get_inst_type(first_inst)
            self.buffer[self.tail]["Dest"] = 
            self.tail += 1 
            if(second_inst != None):



var = ROB()
print(var.check_available())

var.initiate_entries(first_inst, None)
