import socket
from threading import *
import time

DataList= [

",b1111111,kistargyalo",",b1111111,kistargyalo"
,",b1111111,kistargyalo",",b1111111,kistargyalo"
,",b1111111,kistargyalo",",b1111111,kistargyalo"
,",b1111111,kistargyalo",",b1111112,kistargyalo"
,",b1111112,kistargyalo",",b1111112,kistargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,nagytargyalo",",b1111111,nagytargyalo"
,",b1111111,iroda",",b1111111,iroda"
,",b1111111,iroda",",b1111111,iroda"
,",b1111111,iroda",",b1111111,iroda"
,",b1111111,iroda",",b1111111,iroda"
,",b1111111,iroda",",b1111111,iroda"
,",b1111112,mernok1",",b1111112,mernok1"
,",b1111111,mernok1",",b1111111,mernok1"
,",b1111111,mernok1",",b1111111,mernok1"
,",b1111111,mernok1",",b1111111,mernok1"
,",b1111111,mernok1",",b1111111,mernok1"
,",b1111111,mernok1",",b1111111,mernok1"
,",b1111111,mernok2",",b1111111,mernok2"
,",b1111111,mernok2",",b1111111,mernok2"
,",b1111111,mernok2",",b1111111,mernok2"
,",b1111111,mernok2",",b1111111,mernok2"
,",b1111111,mernok2",",b1111111,mernok2"
,",b1111111,ebedlo",",b1111111,ebedlo"
,",b1111111,ebedlo",",b1111111,ebedlo"
,",b1111111,ebedlo",",b1111111,ebedlo"
,",b1111111,ebedlo",",b1111111,ebedlo"
,",b1111111,ebedlo",",b1111111,ebedlo"
,",b1111111,ebedlo",",b1111111,ebedlo"

           ]


serversocket = socket.socket()
host = socket.gethostname()
print
port = 4242
print (host)
print (port)
serversocket.bind((host, port))


class client(Thread):

    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        time.sleep(5)
        self.start()

    def run(self):
        index = 0
        while 1:
            self.sock.send(DataList[index])

            print "Data sent to client: ", DataList[index] , type(DataList[index] )
            index = index +1
            if(index== len(DataList)-1):
                index =0
            time.sleep(0.5)


serversocket.listen(5)
print ('server started and listening')

while 1:
    clientsocket, address = serversocket.accept()
    print address
    client(clientsocket, address)
