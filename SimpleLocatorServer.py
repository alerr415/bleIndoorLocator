import thread
import socket
import ScannedData
import time
import Buffer

PiList = {
    '1': "mernok1",
    '2': "ebedlo",
    '3': "mernok2",
    '4': "kistargyalo",
    '5': "nagytargyalo",
    '6': "iroda",
}

scannedData = ScannedData.ScannedData()


def evaluate(clientsocket, addr):
    print "Visualisation connected"
    BufferList = Buffer.PiBuffer()
    while True:
        time.sleep(2)
        try:
            evaluatedlist = scannedData.evaluateAll()
            for x in range(len(evaluatedlist)):  # where the server thinks the phones are from raw data
                message = evaluatedlist[x][0] + "," + PiList[evaluatedlist[x][1][0]] + ","
                #print message
                BufferList.addtobuffer(evaluatedlist[x][0], PiList[evaluatedlist[x][1][0]]) # put the data into a buffer , so it can be processed further

            for x in BufferList.evaluate():

                finalmessage = x[0] + "," + x[1] + ","  # and this function returns the mode
                clientsocket.send(finalmessage)         #of those (so 1 rogue data cant go out)
                time.sleep(1)  #my vizualization needs time to process

            scannedData.clearList()
            time.sleep(0.2)

        except IndexError:
            pass


def on_new_client(clientsocket, addr):   # each raspberry gets a thread
    print("new thread opened for: ", addr)
    while True:
        msg = clientsocket.recv(1024)
        arr = msg.split(';')
        piId, UserId, RSSI = list(arr[0])[3], arr[1], float(''.join(list(arr[2])[1:3]))
        if RSSI < 20:   # if rssi is under 20 , its an anomaly
            RSSI = 100

        if RSSI >= 90:  # above 90 is basically immeasurable
            RSSI = 100

        record = [piId, RSSI, UserId]
        scannedData.addrecord(record)
        time.sleep(0.2)
    clientsocket.close()


s = socket.socket()
host = socket.gethostname()
port = 4242

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))

vizualization = ('10.20.10.216')
while True:
    s.listen(5)
    c, addr = s.accept()
    if addr[0] == vizualization:
        thread.start_new_thread(evaluate, (c, addr))
    else:
        print 'Got connection from', addr
        thread.start_new_thread(on_new_client, (c, addr))
