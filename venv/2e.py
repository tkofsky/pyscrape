import os
import re
from pathlib import Path
import sys
import imaplib
import quopri
import getpass
import email
import email.header
import datetime
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup
import os
import calendar
import shutil


htmldir = r'c:\Users\kofsk\OneDrive\Desktop\tdr html3 start oct4 2020\twoe.txt'

#htmldir = r'C:\Users\kofsk\OneDrive\Desktop\wg'
filename = 'wg.txt'

#thehtmlfile = os.path.join(htmldir, filename)


xcount = 0

fp = open(filename, 'w')





for filename in os.listdir(htmldir):
    if "Copy" not in filename:
        # filename="r90255022.htm"

        print(filename)
        xcount = xcount + 1
        thehtmlfile = os.path.join(htmldir, filename)

        thehtmlfile = os.path.join(htmldir, filename)
        soup = BeautifulSoup(open(thehtmlfile), "html.parser")

        desciptionflagtwoe = ""
        desciptionflagtwod = ""
        mark = soup.find_all(attrs={"name": "mrk"})
        sn = soup.find_all(attrs={"name": "serno"})
        if "section 2(e" in (soup.text.lower()):
            desciptionflagtwoe = "2(e)"

        if "section 2(e)" in (soup.text.lower()): # wolf greenfield
        #if "section 2(d) refusal" in (soup.text.lower()):  # wolf greenfield

            fp.write(filename)
            shutil.copy(thehtmlfile, filename)
        thedate = ""
        theapplicant = ""
        theemail = ""
        email = ""

        xdate = soup.text

        match = re.search('\w{3,9}?\s\d{1,2}?,\s\d{4}?', xdate, re.IGNORECASE)
        match = re.search('\w{3,9}?\s\d{2}?,\s\d{4}?', xdate, re.IGNORECASE)
        if match:
            thedate = match.group(0)
            tmpdate = thedate.replace(" ", "-")
            thedate = tmpdate.replace(",", "")
            if thedate.find("USP") != -1:
                thedate = ''

        # if thedate.find()
        # thedate="Dec-11-2020"

        if thedate == '':
            thedate = 'xxx'

        # thedate=soup.find("div", {"id": "docDateField"})



        if len(desciptionflagtwoe) > 0:

         showrow="yes"
            # fp.write(str(serialnumber) + "|" + str(thedate) + "|" + str(theapplicant) + "|" + str(themark) + "|" + str(addr1) + " " + str(addr2) + " " + str(addr3) + " " + str(addr4) + " " + str(addr5) + "|" + str(email)+"\n")
          #  fp.write( serialnumber + "|" + str(thedate) + "|" + str(themark) + "|" + str(theapplicant) + "\n")
            # fp.write("\n"+str(serialnumber)+"|"+str(themark)+"|"+str(addr1)+" "+str(addr2)+" "+str(addr3)+str(addr4)+" "+str(addr5)+"|"+str(email)+"|"+str(theapplicant)+"|"+str(thedate))
            #print(serialnumber + "|" + str(thedate) +"|" + str(themark) + "|" + str(theapplicant))

