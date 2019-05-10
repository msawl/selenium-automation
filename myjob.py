import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')#this opens the browser
browser.get("http://www.google.com")#tells the browser which page to go to
elem = browser.find_element_by_name("q")#we get the element by name
elem.send_keys('AAPL')#fills out form with our query
elem.send_keys(Keys.RETURN)#simulates pressing the enter key
links = browser.find_elements_by_xpath("//div[@class='rc']//div[@class='r']//a")
for link in links:    
    print([link.text , link.get_attribute("href")]) 