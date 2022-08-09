_author__ = 'User'
import csv
import re
import requests
import fileinput
import io
import shutil
import time
import os
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import urllib.request
import urllib

count = 1


#####################################################################
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handlest
    converter.close()
    fake_file_handle.close()

    if text:
        return text




###############################


####################################################################################
text_file = open("proseemail.csv", "a", encoding='latin-1', errors='replace')  # out
# with open('prose.csv', encoding='latin-1') as f:  #in

with open('prose.csv', 'r') as fi:
    # lines = [line for line in f][:4]

    # sreader=csv.reader(f, delimiter=',', quotechar='"')

    for line in fi:

        one = [None] * 4
        two = [None] * 4
        three = [None] * 4
        serialnum = [None] * 4
        five = [None] * 4
        six = [None] * 4
        seven = [None] * 4
        theemail = [None] * 4
        rangecount=1

        line1 = line#fi.readline()
        rangecount=0
        if line1:
            nn = line1.split(",")
            one[0] = nn[0]
            two[0] = nn[1]
            three[0] = nn[2]
            serialnum[0] = nn[3]
            five[0] = nn[4]
            six[0] = nn[5]
            seven[0] = nn[6]
            rangecount += 1

            theemail[0] = ''

        line2 = fi.readline()
        if line2:
            nn = line2.split(",")
            one[1] = nn[0]
            two[1] = nn[1]
            three[1] = nn[2]
            serialnum[1] = nn[3]
            five[1] = nn[4]
            six[1] = nn[5]
            seven[1] = nn[6]
            rangecount += 1

            theemail[1] = ''


        line3 = fi.readline()
        if line3:
            nn = line3.split(",")
            one[2] = nn[0]
            two[2] = nn[1]
            three[2] = nn[2]
            serialnum[2] = nn[3]
            five[2] = nn[4]
            six[2] = nn[5]
            seven[2] = nn[6]
            rangecount += 1
        theemail[2] = ''

        line4 = fi.readline()
        if line4:

            nn = line4.split(",")
            one[3] = nn[0]
            two[3] = nn[1]
            three[3] = nn[2]
            serialnum[3] = nn[3]
            five[3] = nn[4]
            six[3] = nn[5]
            seven[3] = nn[6]
            rangecount += 1
        theemail[3] = ''

        # time.sleep(2)
        url = 'https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=' + str(serialnum[0]) + "," + str(serialnum[1]) + "," + str(serialnum[2]) + "," + str(serialnum[3])+'&type=nop'
        print(url)
        payload = {}
        headers = {
            'USPTO-API-KEY': 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsIng1dCI6Inp2UGxaU0dkVnBRdWRYc3JMcGR1c1Vfc05wayIsImtpZCI6Im9yYWtleSJ9.eyJzdWIiOiJtZWxhbmllX2VsYW5hQHlhaG9vLmNvbSIsIm9yYWNsZS5vYXV0aC51c2VyX29yaWdpbl9pZF90eXBlIjoiTERBUF9VSUQiLCJvcmFjbGUub2F1dGgudXNlcl9vcmlnaW5faWQiOiJtZWxhbmllX2VsYW5hQHlhaG9vLmNvbSIsImlzcyI6Ind3dy5vcmFjbGUuZXhhbXBsZS5jb20iLCJvcmFjbGUub2F1dGguc3ZjX3BfbiI6Ik9BdXRoU2VydmljZVByb2ZpbGUiLCJpYXQiOjE1OTEzNjIzOTcsIm9yYWNsZS5vYXV0aC5wcm4uaWRfdHlwZSI6IkxEQVBfVUlEIiwib3JhY2xlLm9hdXRoLnRrX2NvbnRleHQiOiJyZXNvdXJjZV9hY2Nlc3NfdGsiLCJleHAiOjE2MDY5MTQzOTcsInBybiI6Im1lbGFuaWVfZWxhbmFAeWFob28uY29tIiwianRpIjoiY2YzZTE5ZmMtNGVlNC00ODI4LTk3OWItZWFhMTgxZjE4NzRmIiwib3JhY2xlLm9hdXRoLmNsaWVudF9vcmlnaW5faWQiOiJSQkFDU2VydmljZXNPQXV0aEFQSUtleUNsaWVudCIsIm9yYWNsZS5vYXV0aC5zY29wZSI6IlRTRFJBUEkuUkVBRCIsInVzZXIudGVuYW50Lm5hbWUiOiJEZWZhdWx0RG9tYWluIiwib3JhY2xlLm9hdXRoLmlkX2RfaWQiOiIxMjM0NTY3OC0xMjM0LTEyMzQtMTIzNC0xMjM0NTY3ODkwMTIifQ.KesnbgQn_VzLhoCBk8KFbZ5YFUfCffBjqPOoxyrtRFMwrwbKo2x8Bopa5-gQJY6Ar8Z57gikkxzHAk2YkJnVKw71x9p8Q0FrVh2_hDt-ThBmMELVj2d2egZ2i3r6aShzv0iJv6WX1lMtANUNQSYnPwCGa8bMZr-Wm6sp866U0OM',
            'Cookie': 'StackCookie='}

        if count > 3:
            time.sleep(45)
            count = 0
        r = requests.request("GET", url, headers=headers, data=payload)
        time.sleep(.5)
        count += 1
        if os.path.exists("temp.pdf"):
            os.remove("temp.pdf")
            time.sleep(2)
        with open('temp.pdf', 'wb') as f:
            f.write(r.content)

            time.sleep(3)
            pdfsize = os.path.getsize("temp.pdf")
            alldocs = ""
            if pdfsize > 150:
                alldocs = extract_text_from_pdf('temp.pdf')

            print(alldocs)
            alldocs = alldocs.replace("-", "")
            alldocs = alldocs.replace(",", "")
            alldocs = alldocs.replace("TMOfficialNotices@USPTO.GOV", "")
            alldocs = alldocs.replace("TMPostPubQuery@uspto.gov.", "")
            alldocs = alldocs.replace("TrademarkAssistanceCenter@uspto.gov.", "")

            alldocs = alldocs.replace("From:", "SPLIT")
            alldocs = alldocs.replace("Commissioner for", "SPLIT")
            alldocs = alldocs[alldocs.find("SPLIT") + 5:]
            sections = alldocs.split("SPLIT")

            
            for k in range(rangecount):
                for sp in sections:  # loop through serialnums
                    
                    if serialnum[k] in sp:  # if sn found in that section
                        foundsection = sp

                        match = re.search(r'[\w\.-]+@[\w\.-]+', foundsection)
                        if match:
                            theemail[k] = match.group(0)

                        break
                theemail[k]=theemail[k].lower()
                if ".com" in theemail[k]:
                    ind = theemail[k].index('.com')
                    slen = len(theemail[k])
                    if slen - ind > 6:
                        theemail[k] = theemail[k][0:ind + 4]

                if ".net" in theemail[k]:
                    ind = theemail[k].index('.net')
                    slen = len(theemail[k])
                    if slen - ind > 6:
                        theemail[k] = theemail[k][0:ind + 4]

                newline = one[k] + "," + theemail[k] + "," + three[k] + "," + serialnum[k] + "," + five[k] + "," + six[k] + ',' + seven[k]
                print(newline)
                text_file.write(newline)

                # xsec=nn[9]
            f.close()
            text_file.flush()
            os.fsync(text_file.fileno())


text_file.close()

###################################################################
















