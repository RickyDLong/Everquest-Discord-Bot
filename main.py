from discord import Webhook, RequestsWebhookAdapter
import time
import os
import glob

#Working directory of the Everquest Log files
directory = 'E:\\Project1999\\Logs\\eqlog_Virx_project1999.txt'

#Grabbing the latest file in the Everquest Log Directory
fileName = max(glob.iglob(directory), key=os.path.getctime)

#Collecting the last line of the specified log file.
#Returns the last line of the file in real time
def follow(theFile):
    theFile.seek(0, os.SEEK_END)
    while True:
        line = theFile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


#Tries to distinguish item names typed in chat and return when one is found.
def findItems():
    #Initiate an item list
    items = []
    #Initiates follow() to trail the chat log
    logfile = open('Item List.txt')
    #Loop that watches the last log line and adds it to the items list.
    for item in logfile:
        if(item.strip() == ""):
            continue
        if(not item.rstrip() in items):
            items.append(item.rstrip())
    return items


def main():
    items = findItems()
    logfile = open(fileName)
    loglines = follow(logfile)
    for logline in loglines:
        word = logline.split(" ")
        #If keyword 'auctions,' isn't in the string, ignore it.
        if(word[6]!= 'auctions,'):
            continue
        print(logline.rstrip())
        for item in items:
            #Ignore case
            if logline.upper().find(item.upper())>0:
                print(f"  {item}")

if __name__=="__main__":
    main()




