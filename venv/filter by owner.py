author__ = 'User'
import csv
import re
import requests
from bs4 import BeautifulSoup
import fileinput
from bs4 import BeautifulSoup



with open('owners.txt', 'r') as file: # open the list of owners given by firm
    txt = file.read() #reads the full file in string

text_file = open("xfiltered.csv", "w") # open the file to be written to with only filter owners
with open('newCSV.dat','r') as f:


    text_file.write("Corresp|Owner Cited|Mark Cited|Mark Refused|Owner Refused|Serial No. Cited|Serial No. Refused\n")

    for line in f: # read line by line the csv 2d file
        csvline= line
        sp=csvline.split("|")
        ownercsv=sp[1]+" "
        ownercsv = ownercsv.replace(",", " ")
        ownercsv = ownercsv.lower()
        ownercsv = ownercsv.replace(" corp ", " ")
        ownercsv = ownercsv.replace(" corporation", " ")
        ownercsv = ownercsv.replace(" inc ", " ")
        ownercsv = ownercsv.replace(" llc", " ")
        ownercsv = ownercsv.replace(" llp", " ")
        ownercsv = ownercsv.replace(" p.c.", " ")
        ownercsv = ownercsv.replace(" co ", " ")
        ownercsv = ownercsv.replace(".", " ")
        ownercsv = ownercsv.replace(",", " ")
        ownercsv = ownercsv.replace("&", " ")
        ownercsv = ownercsv.replace("  ", " ")
        ownercsv = ownercsv.replace("  ", " ")
        spo=ownercsv.split(" ") # take only the first two words of owner name

        if len(spo)>=2:
            owner=spo[0]+" "+spo[1]
        else:
            owner=spo[0]


        print (owner)
        owner = owner.replace("  ", " ").strip()+" "

        if "\n"+owner.lower() in "\n"+txt.lower(): # check if owner from csv2d is in the list of owners given by firm
            text_file.write(csvline)




text_file.close()