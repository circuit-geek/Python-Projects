from selenium import webdriver
from lxml import html
from time import sleep
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.in/")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("edifice casio watches for men")
search.send_keys(Keys.ENTER)




