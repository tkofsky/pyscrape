import csv
import re
import requests
import io
import time

_author__ = 'User'

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

#rererer
#####################################################################
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handlest
    converter.close()
    fake_file_handle.close()

    if text:
        return text


hash = {}


def fetch_email(comma_separated_serial_num, count=0, temp_hash={}):
    if count > 2:
        return
    try:
        comma_separated_serial_num = comma_separated_serial_num[:-1]
        get_url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + comma_separated_serial_num + "&type=nop"
        payload = {}
        headers = {
            'USPTO-API-KEY': 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsIng1dCI6Inp2UGxaU0dkVnBRdWRYc3JMcGR1c1Vfc05wayIsImtpZCI6Im9yYWtleSJ9.eyJzdWIiOiJtZWxhbmllX2VsYW5hQHlhaG9vLmNvbSIsIm9yYWNsZS5vYXV0aC51c2VyX29yaWdpbl9pZF90eXBlIjoiTERBUF9VSUQiLCJvcmFjbGUub2F1dGgudXNlcl9vcmlnaW5faWQiOiJtZWxhbmllX2VsYW5hQHlhaG9vLmNvbSIsImlzcyI6Ind3dy5vcmFjbGUuZXhhbXBsZS5jb20iLCJvcmFjbGUub2F1dGguc3ZjX3BfbiI6Ik9BdXRoU2VydmljZVByb2ZpbGUiLCJpYXQiOjE1OTEzNjIzOTcsIm9yYWNsZS5vYXV0aC5wcm4uaWRfdHlwZSI6IkxEQVBfVUlEIiwib3JhY2xlLm9hdXRoLnRrX2NvbnRleHQiOiJyZXNvdXJjZV9hY2Nlc3NfdGsiLCJleHAiOjE2MDY5MTQzOTcsInBybiI6Im1lbGFuaWVfZWxhbmFAeWFob28uY29tIiwianRpIjoiY2YzZTE5ZmMtNGVlNC00ODI4LTk3OWItZWFhMTgxZjE4NzRmIiwib3JhY2xlLm9hdXRoLmNsaWVudF9vcmlnaW5faWQiOiJSQkFDU2VydmljZXNPQXV0aEFQSUtleUNsaWVudCIsIm9yYWNsZS5vYXV0aC5zY29wZSI6IlRTRFJBUEkuUkVBRCIsInVzZXIudGVuYW50Lm5hbWUiOiJEZWZhdWx0RG9tYWluIiwib3JhY2xlLm9hdXRoLmlkX2RfaWQiOiIxMjM0NTY3OC0xMjM0LTEyMzQtMTIzNC0xMjM0NTY3ODkwMTIifQ.KesnbgQn_VzLhoCBk8KFbZ5YFUfCffBjqPOoxyrtRFMwrwbKo2x8Bopa5-gQJY6Ar8Z57gikkxzHAk2YkJnVKw71x9p8Q0FrVh2_hDt-ThBmMELVj2d2egZ2i3r6aShzv0iJv6WX1lMtANUNQSYnPwCGa8bMZr-Wm6sp866U0OM',
            'Cookie': 'StackCookie='}
        print("url is : " + get_url)
        r = requests.request("GET", get_url, headers=headers, data=payload)
        with open('temp.pdf', 'wb') as ff:
            ff.write(r.content)

        get_email_str = extract_text_from_pdf('temp.pdf')
        print("get_email_str: "+get_email_str)
        pages = get_email_str.split("")[:-1]
        for page in pages:
            try:
                print("OKAY: "+page)
                serial_num = page.split("Serial")[1].split("Mark")[0]
                serial_num = str(re.sub('[^0-9]', '', serial_num))
                if (len(serial_num) > 8):
                    serial_num = serial_num[:8]
                emails = page.split("Email Address")[1].split(":")[1].strip().split("@")
                final_email = emails[0] + "@" + emails[1].split(".")[0] + "." + emails[1].split(".")[1][:3]
                if serial_num in hash:
                    temp_hash[serial_num] = True
                    hash[serial_num].append(final_email)
                print("OKAY_1 : " + serial_num + " -> " + final_email)
            except:
                try:
                    if "To:" in page:
                        print("FETCHING EMAIL FROM To:  "+serial_num)
                        emails = page.split("To:")[1].strip().split("@")

                        final_email = emails[0] + "@" + emails[1].split(".")[0] + "." + emails[1].split(".")[1][:3]
                        if serial_num in hash:
                            temp_hash[serial_num] = True
                            hash[serial_num].append(final_email)
                        print("OKAY_1 : " + serial_num + " -> " + final_email)
                except:
                    print("Email is not present in To Even")
                print("Exception in Page")
    except:
        print("Exception "+get_url+ " : " + str(r))
        count += 1
        if r.status_code == 429:
            time.sleep(120)
            comma_separated_serial_num = comma_separated_serial_num + ","
            return fetch_email(comma_separated_serial_num, count, temp_hash)

    print("TEMP HASH "+ str(temp_hash))



####################################################################################

with open('prose.csv', encoding='latin-1') as f:  # in
    sreader = csv.reader(f, delimiter=',', quotechar='"')
    count = 0
    comma_separated_serial_num = ""
    temp_hash = {}
    for row in sreader:
        print(row, count)
        serial_num = row[3]
        hash[serial_num] = [row]
        if (len(serial_num) > 0 and serial_num.startswith("zz") == False):
            count += 1
            comma_separated_serial_num += serial_num + ','
            temp_hash[serial_num] = False
        if (count == 20):
            fetch_email(comma_separated_serial_num, 0, temp_hash)
            time.sleep(60)
            count = 0
            comma_separated_serial_num = ""

    if len(comma_separated_serial_num) > 0:
        fetch_email(comma_separated_serial_num, 0, temp_hash)

text_file = open("proseemail.csv", "w", encoding='latin-1',errors='replace')
for key in hash:
    value = hash[key]
    row = value[0]
    if (len(value) > 1):
        row[1] = value[1]
    content = ",".join(row)+"\n"
    text_file.write(content)
text_file.close()
hash = {}