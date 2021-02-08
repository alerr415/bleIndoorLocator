import UserVars
from Configuration import Config
Configuration = Config()

class ScannedData:
    d1 = list()

    def addrecord(self, var):
        var = Config.Configurate(var)
        record = [var[0], var[1]]
        if not self.d1:
            newUser1 = UserVars.User(var[2], record)
            self.d1.append(newUser1)

        found = False

        for x in self.d1:
            if x.userId == var[2]:
                x.PiData.append(record)
                found = True

        if not found:
            newUser = UserVars.User(var[2], record)
            self.d1.append(newUser)

    def evaluateAll(self):
        a = list()
        for x in self.d1:
            a.append(x.evaluate())

        return a

    def clearList(self):
        while(len(self.d1)>0):
            self.d1.pop()





