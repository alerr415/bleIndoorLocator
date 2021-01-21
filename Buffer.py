import statistics
from statistics import mode


class PiBuffer:
    Roombuffer = list()

    def addtobuffer(self,id,room):
        #print self.Roombuffer
        if not self.Roombuffer:
            self.Roombuffer.append([[id,room]])
        else:
            for x in self.Roombuffer:
                if x[0][0] ==id:
                    if(len(x)>5):
                        x.pop(0)
                    x.append([id,room])
                    return
            self.Roombuffer.append([[id, room]])

    def evaluate(self):
        message = list()
        rooms = list()
        for x in self.Roombuffer:
            for y in x:
                rooms.append(y[1])
                try:
                    message.append([x[0][0] ,mode(rooms)])
                except:
                    print "ugyanannyi jo es rossz ertek"
        print rooms
        return message


