from Multipliers import *
from NAND import NAND
from Multipliers import *
from Adders import *
from BEQ import *
from JMP import *
from LW import *
from SW import *

class RS:
    def __init__(self, station_num):
        self.ebreak = False
        self.station_num = station_num
        #self.station_num["ebreak"][0] = 1
        self.index = {}
        self.index["lw"] = 0
        self.index["sw"] = self.index["lw"] + self.station_num["lw"][0]
        self.index["jmp"] = self.index["sw"] + self.station_num["sw"][0]
        #self.index["jalr"] = self.index["sw"] + self.station_num["sw"]
        #self.index["ret"] = self.index["sw"] + self.station_num["sw"]
        self.index["beq"] = self.index["jmp"] + self.station_num["jmp"][0]
        self.index["add"] = self.index["beq"] + self.station_num["beq"][0]
        #self.index["sub"] = self.index["beq"] + self.station_num["beq"]
        #self.index["addi"] = self.index["beq"] + self.station_num["beq"]
        self.index["nand"] = self.index["add"] + self.station_num["add"][0]
        self.index["mult"] = self.index["nand"] + self.station_num["nand"][0]
        self.index["ebreak"] = self.index["mult"] + self.station_num["mult"][0]

        self.used = {}
        self.used["lw"] = 0
        self.used["sw"] = 0
        self.used["jmp"] = 0
        self.used["beq"] = 0
        self.used["add"] = 0
        self.used["nand"] = 0
        self.used["mult"] = 0
        self.used["ebreak"] = 0
        
        self.cycle = {}
        self.cycle["lw"] = 0
        self.cycle["sw"] = 0
        self.cycle["jmp"] = 0
        self.cycle["beq"] = 0
        self.cycle["add"] = 0
        self.cycle["nand"] = 0
        self.cycle["mult"] = 0
        self.cycle["ebreak"] = 0

        self.station = []

        for i in range(self.station_num["lw"][0]):
            station_entry = {}
            station_entry["name"] = "lw" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = -1
            station_entry["Qk"] = -1
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            station_entry["funct_unit"] = LW(station_num["lw"][1])
            self.station.append(station_entry)

        for i in range(self.station_num["sw"][0]):
            station_entry = {}
            station_entry["name"] = "sw" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = -1
            station_entry["Qk"] = -1
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            station_entry["funct_unit"] = SW(station_num["sw"][1])
            self.station.append(station_entry)

        for i in range(self.station_num["jmp"][0]):
            station_entry = {}
            station_entry["name"] = "jmp" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = -1
            station_entry["Qk"] = -1
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            station_entry["funct_unit"] = JMP(station_num["jmp"][1])
            self.station.append(station_entry)

        for i in range(self.station_num["beq"][0]):
            station_entry = {}
            station_entry["name"] = "beq" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = -1
            station_entry["Qk"] = -1
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            station_entry["funct_unit"] = BEQ(station_num["beq"][1]) #TODO change the 1 to be variable 
            self.station.append(station_entry)

        for i in range(self.station_num["add"][0]):
            station_entry = {}
            station_entry["name"] = "add" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = -1
            station_entry["Qk"] = -1
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            station_entry["funct_unit"] = Adders(station_num["add"][1])
            self.station.append(station_entry)

        for i in range(self.station_num["nand"][0]):
            station_entry = {}
            station_entry["name"] = "nand" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = -1
            station_entry["Qk"] = -1
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            station_entry["funct_unit"] = NAND(station_num["nand"][1])
            self.station.append(station_entry)

        for i in range(self.station_num["mult"][0]):
            station_entry = {}
            station_entry["name"] = "mult" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = -1
            station_entry["Qk"] = -1
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            station_entry["funct_unit"] = Multipliers(station_num["mult"][1])
            self.station.append(station_entry)

        station_entry = {}
        station_entry["name"] = "ebreak"
        station_entry["busy"] = False
        station_entry["op"] = "init"
        station_entry["Vj"] = 0
        station_entry["Vk"] = 0
        station_entry["Qj"] = -1
        station_entry["Qk"] = -1
        station_entry["dest"] = 0
        station_entry["A"] = 0
        station_entry["status"] = "init"
        station_entry["funct_unit"] = None
        self.station.append(station_entry)

    def update_station(self, name, index, busy, op, Vj, Vk, Qj, Qk, dest, A, status):
        self.station[self.index[name] + index]["busy"] = busy
        self.station[self.index[name] + index]["op"] = op
        self.station[self.index[name] + index]["Vj"] = Vj
        self.station[self.index[name] + index]["Vk"] = Vk
        self.station[self.index[name] + index]["Qj"] = Qj
        self.station[self.index[name] + index]["Qk"] = Qk
        self.station[self.index[name] + index]["dest"] = dest
        self.station[self.index[name] + index]["A"] = A
        self.station[self.index[name] + index]["status"] = status

    def issue(self, name, Vj, Vk, Qj, Qk, dest, A):
        temp=str()
        index = self.cycle["add"] % self.station_num["add"][0] if (name == "add" or name == "sub" or name == "addi") else self.cycle["jmp"] % self.station_num["jmp"][0] if (name == "jmp" or name == "jalr" or name == "ret") else self.cycle[name] % self.station_num[name][0]
        if (name == "ebreak"):
            index = 0
        if (name == "add" or name == "sub" or name == "addi"):
            temp="add"
        elif(name == "jmp" or name == "jalr" or name == "ret"):
            temp="jmp"
        elif(name == "ebreak"):
            temp = "ebreak"
        else: temp=name
        self.station[self.index[temp] + index]["busy"] = True
        self.station[self.index[temp] + index]["op"] = name
        self.station[self.index[temp] + index]["Vj"] = Vj if (Qj == -1 or Qj== "init") else 0
        self.station[self.index[temp] + index]["Vk"] = Vk if (Qk == -1 or Qk== "init") else 0
        self.station[self.index[temp] + index]["Qj"] = -1 if (Qj == -1 ) else Qj
        self.station[self.index[temp] + index]["Qk"] = -1 if (Qk == -1 ) else Qk
        self.station[self.index[temp] + index]["dest"] = dest
        self.station[self.index[temp] + index]["A"] = A
        self.station[self.index[temp] + index]["status"] = "issued"

        if (name == "add" or name == "sub" or name == "addi"):
            self.used["add"] += 1
            self.cycle["add"] += 1
        elif (name == "jmp" or name == "jalr" or name == "ret"):
            self.used["jmp"] += 1
            self.cycle["jmp"] += 1
        else:
            self.used[name] += 1
            self.cycle[name] += 1

    def available(self, name):
        if (name == "add" or name == "sub" or name == "addi"):
            return self.used["add"] < self.station_num["add"][0]
        elif (name == "jmp" or name == "jalr" or name == "ret"):
            return self.used["jmp"] < self.station_num["jmp"][0]
        else:
            return self.used[name] < self.station_num[name][0]

    def ready(self, index):
        return ((self.station[index]["Qj"] == -1) and (self.station[index]["Qk"] == -1) and (self.station[index]["status"] == "issued"))

    def station_num_total(self):
        return self.index["mult"] + self.station_num["mult"][0]

    def execute(self, index, pc):
        self.station[index]["status"] = "executing"
        op = self.station[index]["op"]

        ## Executing the load and store is not done by the provided class. The class calculates the address which isn't the functional unit
        ## of load and store word. The function is to deal with memorey and add data to it and get data from it.

        if(op == "add" or op == "sub"):
            self.station[index]["funct_unit"].operation(self.station[index]["Vj"], self.station[index]["Vk"], self.station[index]["op"])
        elif(op=="addi"):
            self.station[index]["funct_unit"].operation(self.station[index]["Vj"], self.station[index]["A"], self.station[index]["op"])
        elif(op == "jalr" or op == "ret" or op == "jmp"):
            self.station[index]["funct_unit"].operation(self.station[index]["Vj"], self.station[index]["Vk"], self.station[index]["op"], pc)
        elif(op == "nand"):
            self.station[index]["funct_unit"].Nand(self.station[index]["Vj"], self.station[index]["Vk"])
        elif(op == "beq"):
            self.station[index]["funct_unit"].branch(self.station[index]["Vj"], self.station[index]["Vk"], self.station[index]["A"], pc)
        elif(op=="mult"):
            self.station[index]["funct_unit"].mul(self.station[index]["Vj"], self.station[index]["Vk"])
        elif(op == "lw"):
            self.station[index]["funct_unit"].getAddress(self.station[index]["Vj"], self.station[index]["A"])
        elif(op == "sw"):
            self.station[index]["funct_unit"].getAddress(self.station[index]["Vj"], self.station[index]["A"])
        else:
            self.ebreak = True
        #return self.station[index]["op"], self.station[index]["Qj"], self.station[index]["Qk"], self.station[index]["A"], index

    def write(self, index):
        operation=self.station[index]["op"]
        if(operation=="addi" or operation=="sub"):
            operation="add"
        if(operation=="jalr" or operation== "ret"):
            operation= "jmp"
        self.used[operation]-=1
        self.station[index]["busy"] = False
        self.station[index]["op"] = "init"
        self.station[index]["Vj"] = 0
        self.station[index]["Vk"] = 0
        self.station[index]["Qj"] = -1
        self.station[index]["Qk"] = -1
        self.station[index]["dest"] = 0
        self.station[index]["A"] = 0
        self.station[index]["status"] = "init"
        

    def get_status(self, index):
        return self.station[index]["status"]

    def get_type(self, index):
        return self.station[index]["op"]

    def get_Vj(self, index):
        return self.station[index]["Vj"]

    def get_missPridected(self):
        return self.missPridected

    def get_ebreak(self):
        return self.ebreak

    def decFuncUnitCount(self, index):
        if(index == self.index["ebreak"] and self.ebreak):
            return "ebreak"
        if(index != self.index["ebreak"]):
            self.station[index]["funct_unit"].count()
            result = self.station[index]["funct_unit"].ready()
            if self.station[index]["op"] == "beq":
                self.missPridected = self.station[index]["funct_unit"].missPridected()
            if(result != None):
                self.station[index]["status"] = "done"
                return result
            else:
                return None

    def getTargetRob(self, index):
        return self.station[index]["dest"]
    
    def updRS(self, robIndex, result):
        for i in self.station:
            if(i['Qj']==robIndex):
                i['Qj']=-1
                i['Vj']=result
            if(i['Qk']==robIndex):
                i['Qk']=-1
                i['Vk']=result

    def flush(self):
        for i in range(self.index["mult"] + self.station_num["mult"][0]):
            self.station[i]["busy"] = False
            self.station[i]["op"] = "init"
            self.station[i]["Vj"] = 0
            self.station[i]["Vk"] = 0
            self.station[i]["Qj"] = -1
            self.station[i]["Qk"] = -1
            self.station[i]["dest"] = 0
            self.station[i]["A"] = 0
            self.station[i]["status"] = "init"
            self.used["lw"] = 0
            self.used["sw"] = 0
            self.used["jmp"] = 0
            self.used["beq"] = 0
            self.used["add"] = 0
            self.used["nand"] = 0
            self.used["mult"] = 0
            self.used["ebreak"] = 0
            self.cycle["lw"] = 0
            self.cycle["sw"] = 0
            self.cycle["jmp"] = 0
            self.cycle["beq"] = 0
            self.cycle["add"] = 0
            self.cycle["nand"] = 0
            self.cycle["mult"] = 0
            self.cycle["ebreak"] = 0