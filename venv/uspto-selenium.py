import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import csv
import re
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\selenium\chromedriver.exe')
url="https://tsdr.uspto.gov/#caseNumber=88734234&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=documentSearch"
driver.get(url)
time.sleep(2)
el=driver.find_element_by_xpath('//a[contains(@href,"FTK")]')
link=el.get_attribute('href')
linknumber=link.split("=")[2]
url="https://tsdrsec.uspto.gov/ts/cd/casedoc/sn88734234/"+linknumber+"/1/webcontent?scale=1"

driver.get(url)



time.sleep(2)
aa=driver.page_source
match = re.search(r'[\w\.-]+@[\w\.-]+', source)
emailaddress=match[0]
