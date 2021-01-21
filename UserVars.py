from util import *


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



    def KalmanFilterPiData(self):
        KalmanList = list()
        found = False
        for x in self.PiData:
            if not KalmanList:
                KalmanList.append(x[0])
                KalmanList[0].append(x[1])
            for y in range(len(KalmanList)):
                if x[0] == KalmanList[y][0]:
                    KalmanList[y].append(x[1])
                    found = True
            if not found:
                KalmanList[len(KalmanList)].append(x[0])
                KalmanList[len(KalmanList)].append(x[1])
        temp = list()
        for x in KalmanList:
            signal_kalman_filter = kalman_filter(x[1:], A=1, H=1, Q=1.6, R=6)
            x[1:] = signal_kalman_filter
            for y in x[1:]:
                temp.append([x[0],y])

        self.PiData = temp



