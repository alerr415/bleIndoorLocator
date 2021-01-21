
class User:

    def __init__(self, user, pidata):
        self.userId = ""
        self.PiData = list()
        self.userId = user
        self.PiData.append(pidata)

    def clearList(self):
        while len(self.PiData) > 0:
            self.PiData.pop()

    def evaluate(self):  # Returns the closest raspberry
        closest = self.PiData[0]

        for x in self.PiData:
            if closest[1] > x[1]:
                closest = x

        return [self.userId, closest]

    def printlist(self):
        print self.userId, " ", self.PiData
