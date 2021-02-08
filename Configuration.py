import json

class Config:
    data = dict()
# Opening JSON file
    def __init__(self):
        with open('config.json') as json_file:
            self.data = json.load(json_file)




    def Configurate(self,var):
        try:
            var[0] = var[0] + self.data[self.data[var[0]]]
            return var
        except:
            return var

