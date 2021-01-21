import thread
import socket
import ScannedData
import time
import Buffer

PiList = {
    #'0': "Meg nemtom",
    #'1': "mernok1",
    #'2': "mernok2"

    '3': "mernok1",
    '1': "nagytargyalo",
    '2': "mernok2"
}

scannedData = ScannedData.ScannedData()


def evaluate(clientsocket, addr):
    print "Visualisation connected, Start the raspberries now"
    BufferList = Buffer.PiBuffer()
    while True:
        try:
            for x in range(len(scannedData.evaluateAll())):
                message = scannedData.evaluateAll()[x][0] + "," + PiList[scannedData.evaluateAll()[x][1][0]] + ","
                #print message
                BufferList.addtobuffer(scannedData.evaluateAll()[x][0], PiList[scannedData.evaluateAll()[x][1][0]])

            for x in BufferList.evaluate():
                finalmessage = x[0] + "," + x[1] + ","
                clientsocket.send(finalmessage)
                time.sleep(1)


            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            scannedData.clearList()
            time.sleep(0.2)

        except IndexError:
            print("No data received yet ")




def on_new_client(clientsocket, addr):
    print("new thread opened for: ", addr)
    while True:
        msg = clientsocket.recv(1024)
        arr = msg.split(';')
        piId, UserId, RSSI = list(arr[0])[3], arr[1], float(''.join(list(arr[2])[1:3]))
        if RSSI < 20:
            RSSI = 100

        if RSSI >= 90:
            RSSI = 100

        record = [piId, RSSI, UserId]
        #print record
        scannedData.addrecord(record)
        time.sleep(0.2)
    clientsocket.close()


s = socket.socket()
host = socket.gethostname()
port = 4242

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))
s.listen(5)
c, addr = s.accept()
thread.start_new_thread(evaluate, (c, addr))

while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    thread.start_new_thread(on_new_client, (c, addr))
