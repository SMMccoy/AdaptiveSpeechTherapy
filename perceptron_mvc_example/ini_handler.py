import json

class ini():
    def __init__(self) -> None:
        ini_file_read = open("~/ini.py","r")
        ini_file_read.close()
        self.ini_dict = json.loads(ini_file_read.read())
    def getLevel(self):
        return self.ini_dict["level"]
    def setLevel(self,level):
        self.ini_dict["level"] = level
    def endSession(self):
        ini_file_write = open("~/ini.py","w")
        ini_file_write.write(json.dumps(self.ini_dict))
        ini_file_write.close()
        
