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
from shutil import copyfile

htmldir = 'c:\weekly tsdr'
filename = 'refusalforeign.txt'
thehtmlfile = os.path.join(htmldir, filename)

htmldir = 'c:\weekly tsdr'
filename = 'refusaldomestic.txt'
thehtmlfilerefused = os.path.join(htmldir, filename)




htmldir=r'C:\Users\User\Desktop\TDR HTML3-April 2019 to April 13 2020\newhtm'



for filename in os.listdir(htmldir):
    if filename.endswith(".htm"):
        # filename="r79289909.htm"

        print(filename)

        thehtmlfile = os.path.join(htmldir, filename)

        thehtmlfile = os.path.join(htmldir, filename)
        dst = 'c:/weekly tsdr/keep3/'+filename
        ####src = 'c:/weekly tsdr/'+filename
        src = thehtmlfile
        #with open(src, "rb") as f1:
        #    with open(dst, "wb") as f2:
        #        f2.writelines(f1.readlines())



        soup = BeautifulSoup(open(thehtmlfile), "html.parser")

        # get date using tr td
        # table = soup.find_all('table')
        # rows = table[3].find_all('tr')
        # for row in rows:

        othertext = "prior-filed"  # sometimes it says no pending or reg, but then it saysHowever, a mark in a prior-filed pending application may present a bar to registration of applicant’s mark.

        noconflict = "database of registered and pending marks and has found no"  # found no conflicting marks"# that would bar registration under Trademark Act Section 2(d)"
        noconflicttwo = "database of registered and pending marks and found no"  # found no conflicting marks"# that would bar registration under Trademark Act Section 2(d)"
        #nonconflictthree = "no similar registered or pending marks"

        # noconflict="found no"
        desciptionflag = ''
        desciptionflagtwoe = ""
        desciptionflagtwod = ""
        desciptionflagcbd = ""
        desciptionflagdc = ""

        if "section 2(d" in (soup.text.lower()):
            if noconflict in (soup.text.lower()) or noconflicttwo in (soup.text.lower()):  # if 2d happens top be there because due to the phrase above then
               if "the filing date of pending" in (soup.text.lower()):
                 desciptionflagtwod = " 2(d)"
                 try:
                    copyfile(src, dst)
                    print(src, dst)
                 except:
                     print ("errror")

               if "prior-filed" in (soup.text.lower()) or "prior filed" in (soup.text.lower()):
                   desciptionflagtwod = " 2(d)"
                   try:
                    copyfile(src, dst)
                    print (src,dst)
                   except:
                        print ("error")
