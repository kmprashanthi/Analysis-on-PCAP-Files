import os

def check(IPprev, IPcurr):
    if (IPprev[0]==IPcurr[0]) and (IPprev[1]==IPcurr[1]) and (IPprev[2]==IPcurr[2]):
        return True
    return False

def writeInFile(IPConcate):
    filenameout = "IPFormatted.txt"
    fileout = open(filenameout,"a")
    fileout.write(IPConcate+'\n')


def appendTillSocketLevel(IPPrev,IPcurr):
    filenameout="IPFormatted.txt"
    file = open(filenameout,"r+")
    prevIP= os.popen("tail -n 1 %s" % filenameout).read().rstrip().rsplit(".")
    if prevIP==[]:
        prevIP = ['0','0','0','0']
    print('PrevIP   ',prevIP)
    IPConcate=''
    if (prevIP!=[]):
        if(check(prevIP,IPPrev)):
            IPConcate=prevIP[0]+'.'+prevIP[1]+'.'+prevIP[2]+'.'
            print ('IPConcate  ', IPConcate)
            for ip in range (3,len(prevIP)):
                IPConcate = IPConcate + prevIP[ip] + '.'
            IPConcate = IPConcate + IPcurr[-1]
            
        else:
            IPConcate = IPPrev[0]+'.'+IPPrev[1]+'.'+IPPrev[2]+'.'+IPPrev[3]+'.'+IPcurr[-1]

    #write something here to delete the last line of the file
    writeInFile(IPConcate)


filenamein = "IPAddresses.txt"
filein = open(filenamein,"r")
IPprev = os.popen("head -n 1 %s" % filenamein).read().rstrip()
IPConcate=''
for line in filein:
    line = line.rstrip()
    IPcurr=line.rsplit(".")
    print(IPcurr)
    if (check(IPprev, IPcurr)):
        appendTillSocketLevel(IPprev,IPcurr)
    else:
        IPConcate = IPcurr[0]+'.'+IPcurr[1]+'.'+IPcurr[2]+'.'+IPcurr[3]
        writeInFile(IPConcate)
    IPprev=IPcurr


   

