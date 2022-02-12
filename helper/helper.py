import re
import csv

#Pastes the garbage raw copied format from wiki.project1999 into an item name only file
def grabItemNames():
    file = open('Every 2.txt', "r").readlines()[0::2]
    with open('../Item List.txt', "w") as f:
        writer = csv.writer(f)
        writer.writerow(file)

#Clean up the item names and take out any unneccesary characters
def cleanUp(fileName):
    fileIn = open(fileName, 'rt')
    fileOut = open('_Spells.txt', "wt")
    for line in fileIn:
        fileOut.write(line.replace("_", " "))
    fileIn.close()
    fileOut.close()

#Opens .txt file and places each line item in a set
#Outputs new file with zero duplicates
def findDuplicates(fileName):
    lines_seen = set()
    outFile = open('../Item List.txt', "wt")
    inFile = open(fileName, 'rt')
    for line in inFile:
        print(line)
        if(line not in lines_seen): #Not a duplicate line
            outFile.write(line)
            lines_seen.add(line)
    outFile.close()

def extractItemName(fileName):
    outFile = open('../Item List.txt', "wt")
    inFile = open(fileName, "rt")
    for line in inFile:
        index = line.split(" ")


#findDuplicates('Item Names.txt')
#cleanUp("Spells.txt")




