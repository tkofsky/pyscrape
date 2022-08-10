import requests
import csv
import re
import fileinput
import io
import selenium
from selenium import webdriver
import time
import requests


#1212


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
driver = webdriver.Chrome(chrome_options=chrome_options)



#driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\ChromeDriver\chromedriver_win32\chromedriver.exe')

lastline=0
getpage=1
##get last line of file
with open('proseemail.csv', encoding='latin-1') as f:
    for line in f:
        lastline+=1


xcount=1

text_file = open("proseemail.csv", "a", encoding='latin-1',errors='replace')  #out
with open('prose.csv', encoding='latin-1') as f:  #in

    sreader=csv.reader(f, delimiter=',', quotechar='"')

    for row in sreader:


        if lastline>xcount:#start after the last line
            xcount += 1
        else:
            print(row)

            nn = row
            one=nn[0]
            two=nn[1]
            three=nn[2]
            serialnum = nn[3]
            five = nn[4]
            six = nn[5]
            seven = nn[6]
            #time.sleep(2)
            theemail=''
            print (theemail)

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(
                '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
            #driver = webdriver.Chrome(chrome_options=chrome_options)
            if xcount==8:
                xcount=1
            #    driver=webdriver.Firefox()
            #else:

            #driver.session_id = "a2325ref544"+serialnum
            driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')



            #driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
            url = "https://tsdr.uspto.gov/#caseNumber="+serialnum+"&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=documentSearch"
            #driver.delete_all_cookies()
            print (url)
            driver.get(url)

            time.sleep(2)



            source = driver.page_source
            if source.find('=RFA')!=-1:
                el = driver.find_element_by_xpath('//a[contains(@href,"RFA")]')
            if source.find('=FTK')!=-1:
                el = driver.find_element_by_xpath('//a[contains(@href,"FTK")]')
            if source.find('=APP')!=-1:
                el = driver.find_element_by_xpath('//a[contains(@href,"APP")]')

            #driver.close()
            #driver.quit()

            link = el.get_attribute('href')
            linknumber = link.split("=")[2]
            url = "https://tsdrsec.uspto.gov/ts/cd/casedoc/sn"+serialnum+"/" + linknumber + "/1/webcontent?scale=1"

            #driver.get("http://shulamit.com")
            #time.sleep(1)
            getpage+=1
            driver.get(url)
            print (url)
            time.sleep(1)
            source = driver.page_source
            match = re.search(r'[\w\.-]+@[\w\.-]+', source)
            if match:
                theemail = match[0]

            print (theemail)

            driver.close()
            driver.quit()

            newline = one + "," + theemail + "," + three + "," + serialnum + "," + five + "," + six + ',' + seven
            text_file.write("\n" + newline)
            if getpage>3:
                time.sleep(1)
                print ('ended')
                driver.close()
                driver.quit()
                exit()
