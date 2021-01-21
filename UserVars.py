class User:

    def __init__(self, user, pidata):
        self.userId = ""
        self.PiData = list()
        self.userId = user
        self.PiData.append(pidata)

    def clearList(self):
        while len(self.PiData) > 0:
            self.PiData.pop()

    def evaluate(self):  #Visszaadja , hgoy az adott userID ( ember) hez melyik raspberry van a legkozelebb
        legkozelebbi = self.PiData[0]

        for x in self.PiData:                        #x in PiData = [ "pi" , "Rssi"]
              if legkozelebbi[1] > x[1]:
                legkozelebbi = x

        return [self.userId, legkozelebbi]

    def printlist(self):
        print self.userId, " ", self.PiData
