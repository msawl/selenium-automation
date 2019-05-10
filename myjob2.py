import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe')#this opens the browser
browser.get("http://www.indeed.com")#tells the browser which page to go to
elem = browser.find_element_by_name("q")#we get the element by name
elem.send_keys('Software Engineer')#fills out form with our query
elem.send_keys(Keys.RETURN)#simulates pressing the enter key


links = browser.find_elements_by_xpath("//div[@class='title']//a[@class='jobtitle turnstileLink ']")
jobLinks = []
diction = dict()
for link in links: 
    up = dict()
    up.update({'href' :link.get_attribute("href") , 'title' : link.text})	
    jobLinks.append(up)
    	
    #link.click()	

print(jobLinks[1]['href'])

