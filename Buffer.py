import statistics
from statistics import mode


class PiBuffer:
    Roombuffer = list()

    def addtobuffer(self, id, room):
        if not self.Roombuffer:
            self.Roombuffer.append([[id, room]])
        else:
            for x in self.Roombuffer:
                if x[0][0] == id:
                    if len(x) >= 5:
                        x.pop(0)
                    x.append([id, room])
                    return
            self.Roombuffer.append([[id, room]])

    def evaluate(self):
        message = list()

        for x in self.Roombuffer:
            # print self.Roombuffer
            rooms = list()
            for y in x:
                rooms.append(y[1])
            try:

                message.append([x[0][0], mode(rooms)])

            except:
                pass
        print message

        return message


