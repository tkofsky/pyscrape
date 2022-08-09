import requests
import csv
import re
import fileinput
import io
import selenium
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
driver = webdriver.Chrome(chrome_options=chrome_options)

# driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\ChromeDriver\chromedriver_win32\chromedriver.exe')


xcount = 1
text_file = open("proseemail.csv", "w", encoding='latin-1', errors='replace')  # out
with open('prose.csv', encoding='latin-1') as f:  # in

    sreader = csv.reader(f, delimiter=',', quotechar='"')

    for row in sreader:
        xcount += 1
        nn = row
        one = nn[0]
        two = nn[1]
        three = nn[2]
        serialnum = nn[3]
        five = nn[4]
        six = nn[5]
        seven = nn[6]
        # time.sleep(2)
        theemail = ''
        print(theemail)
        if (xcount % 2) == 0:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(
            '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
        else:
            chrome_options.add_argument("User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")


        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # if xcount%2==0:
        #    driver=webdriver.Firefox()
        # else:
        driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')

        # driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
        url = "https://tsdr.uspto.gov/#caseNumber=" + serialnum + "&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=documentSearch"

        driver.get(url)
        time.sleep(2)

        source = driver.page_source
        if source.find('=RFA') != -1:
            el = driver.find_element_by_xpath('//a[contains(@href,"RFA")]')
        if source.find('=FTK') != -1:
            el = driver.find_element_by_xpath('//a[contains(@href,"FTK")]')
        if source.find('=APP') != -1:
            el = driver.find_element_by_xpath('//a[contains(@href,"APP")]')

        # driver.close()
        # driver.quit()

        link = el.get_attribute('href')
        linknumber = link.split("=")[2]

        driver.close()
        driver.quit()
        print (link)
        newline = one + "," + theemail + "," + three + "," + serialnum + "," + five + "," + six + ',' + seven +","+ link
        text_file.write("\n" + newline)
