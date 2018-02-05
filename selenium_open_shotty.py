import sys
sys.path.append('C:\Python27\Lib\site-packages')

import BeautifulSoup

from bs4 import BeautifulSoup
import requests

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Autodesk\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.implicitly_wait(10)
driver.get("https://wise.shottyapp.com/");

username = driver.find_element_by_xpath("//input[@placeholder='Email']")
password = driver.find_element_by_xpath("//input[@placeholder='Password']")

print (username)
print (password)

username.send_keys("stasbasko@gmail.com")
password.send_keys("123456")
button=driver.find_element_by_tag_name("button")
print(button)
button.click()
content = driver.find_element_by_tag_name("body")
print(content.text)


data = content.text
soup = BeautifulSoup(data,'lxml')
for link in soup.find_all('a'):
    print(link.get('href'))