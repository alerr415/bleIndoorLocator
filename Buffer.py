import statistics
from statistics import mode


class PiBuffer:
    Roombuffer = list()

    def addtobuffer(self,id,room):
        if not self.Roombuffer:
            self.Roombuffer.append([[id,room]])
        else:
            for x in self.Roombuffer:
                if x[0][0] ==id:
                    if(len(x)>5):
                        x.pop()
                    x[0].append([id,room])
                    return
            self.Roombuffer.append([[id, room]])

    def evaluate(self):
        message = list()
        for x in self.Roombuffer:
            message.append(mode(x))
        return message

