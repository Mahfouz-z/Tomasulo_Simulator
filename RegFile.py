class RegFile: 
   def __init__(self, ROBNumber, data):
       self.ROBNumber = -1
       self.data = data
       
   def flush(self):
       self.ROBNumber = -1