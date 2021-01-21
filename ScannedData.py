import UserVars


class ScannedData:
    d1 = list()

    def addrecord(self, var):

        record = [var[0], var[1]]
        if not self.d1:
            newUser1 = UserVars.User(var[2], record)
            print "List created"
            self.d1.append(newUser1)

        found = False
        index = 0

        for x in self.d1:
            if x.userId == var[2]:
                x.PiData.append(record)
                found = True
            index = index + 1

        if not found:
            print "New user added"
            newUser = UserVars.User(var[2], record)
            self.d1.append(newUser)

    def evaluateAll(self):
        a = list()
        for x in self.d1:
            a.append(x.evaluate())

        return a

    def clearList(self):
        for x in range(len(self.d1)):
            self.d1[x].clearList()





