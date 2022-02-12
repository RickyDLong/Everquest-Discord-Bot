
import time
import os
import glob
import argparse


#WIP
parser = argparse.ArgumentParser(description='Target Directory')
parser.add_argument('--dir', action='store', dest='dir')
args = parser.parse_args()

#Working directory of the Everquest Log files (Temporary)
directory = 'E:\\Project1999\\Logs\\eqlog_Virx_project1999.txt'

#Grabbing the latest file in the Everquest Log Directory
fileName = max(glob.iglob(directory), key=os.path.getctime)

#Collecting the last line of the specified log file.
#Returns the last line of the file in real time
def follow(theFile):
    try:
        theFile.seek(0, os.SEEK_END)
        while True:
            line = theFile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
    except IOError:
        print("File not found.")

#Returns trailing line from logfile
def getLogLines():
    logfile = open(fileName)
    loglines = follow(logfile)
    return loglines

#Searches through last line of logfile, splits items by " " delimiter
#places into list and returns the player name and items found from findItems()
def findAuction():
    for logline in getLogLines():
        word = logline.split(" ")
        if(word[6]!= 'auctions,'):
            continue
        charName = word[5]
        print(logline.rstrip())
        print(charName)
        for item in findItems():
            if logline.upper().find(item.upper())>0:
                print(f"  {item}")





#Searches through log file, finds last line, compares string
#to logfile object and returns found objects.
def findItems():
    items = []
    logfile = open('Item List.txt')
    for item in logfile:
        if(item.strip() == ""):
            continue
        if(not item.rstrip() in items):
            items.append(item.rstrip())
    return items




if __name__=="__main__":
    findAuction()





