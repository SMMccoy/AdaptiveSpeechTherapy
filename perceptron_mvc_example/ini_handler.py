import json

class ini():
    def __init__(self) -> None:
        ini_file_read = open("ini.json","r")
        self.ini_dict = json.loads(ini_file_read.read())
        ini_file_read.close()
    def getLevel(self):
        return self.ini_dict["level"]
    def setLevel(self,level):
        self.ini_dict["level"] = level
    def endSession(self):
        ini_file_write = open("ini.json","w")
        ini_file_write.write(json.dumps(self.ini_dict))
        ini_file_write.close()
        
