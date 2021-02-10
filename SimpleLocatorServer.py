import thread
import socket
import ScannedData
import time
import Buffer
import  Configuration


PiList = Configuration.Config().data
Conf = Configuration.Config()
scannedData = ScannedData.ScannedData()


def evaluate(clientsocket, addr):
    print "CONF (Time to evaluate: ", Conf.data['TIME_TO_EVALUATE'],')'
    print "Visualisation connected"
    BufferList = Buffer.PiBuffer()
    while True:

        time.sleep(Conf.data['TIME_TO_EVALUATE'])
        try:
            evaluatedlist = scannedData.evaluateAll()
            for x in range(len(evaluatedlist)):  # where the server thinks the phones are from raw data
                message = evaluatedlist[x][0] + "," + PiList[evaluatedlist[x][1][0]] + ","
                #print message
                BufferList.addtobuffer(evaluatedlist[x][0], PiList[evaluatedlist[x][1][0]]) # put the data into a buffer , so it can be processed further

            for x in BufferList.evaluate():   # this function returns the mode of each person's buffer list (so 1 rogue data cant go out)

                finalmessage = x[0] + "," + x[1] + ","
                clientsocket.send(finalmessage)

            scannedData.clearList()

        except IndexError:
            pass


def on_new_client(clientsocket, addr):   # each raspberry gets a thread
    print("new thread opened for: ", addr)
    while True:
        msg = clientsocket.recv(1024)
        arr = msg.split(';')
        piId ,UserId, RSSI = ''.join(list(arr[0])[3:]), arr[1], float(''.join(list(arr[2])[1:3]))

        if RSSI <= Conf.data['MIN_VALUE'] or RSSI >= Conf.data['MAX_VALUE']:  # MIN_VALUE < RSSI < MAX_VALUE
            continue

        record = [piId, RSSI, UserId]
        scannedData.addrecord(record)
        time.sleep(0.2)
    clientsocket.close()


s = socket.socket()
host = socket.gethostname()
port = Conf.data['PORT']
print "CONF (MINIMUM RSSI: ", Conf.data['MIN_VALUE'], ')'
print "CONF (MAXIMUM RSSI: ", Conf.data['MAX_VALUE'], ')'
print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))

vizualization = Conf.data['IP_ADDRESS_OF_PLC']
while True:
    s.listen(5)
    c, addr = s.accept()
    if addr[0] == vizualization:
        thread.start_new_thread(evaluate, (c, addr))
    else:
        print 'Got connection from', addr
        thread.start_new_thread(on_new_client, (c, addr))
