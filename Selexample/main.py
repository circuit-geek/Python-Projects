# from pprint import pprint
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import csv


chrome_driver_path = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.in/s?k=edifice+casio+watches+for+men&crid=X28SFHIGCG1Z&sprefix=edif%2Caps%2C321&ref=nb_sb_ss_ts-doa-p_1_4")

at1=[]
at2=[]
at3=[]
at4=[]
at5=[]
at6=[]

att1=driver.find_elements_by_class_name("s-line-clamp-1")
for i in att1:
    s=i.text
    at1.append(s)
print(at1)

# att2=driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div/div/div[3]/h2/a')
# att2=driver.find_elements_by_css_selector("span.a-size-base-plus a-color-base a-text-normal")
# att2=driver.find_elements_by_class_name("a-price-whole")
att2=driver.find_elements_by_class_name("a-link-normal a-text-normal")
for i in att2:
    print(i.text)


driver.quit()




































# from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
#
#
# chrome_driver_path = "C:\Developement\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("https://www.nobroker.in/")
#
# location = driver.find_element_by_class_name("selectedcity")
# location.click()

# las = driver.find_element_by_name("lName")
# last.send_keys("Prasanna")
#
# email = driver.find_element_by_name("email")
# email.send_keys("gaurav@gaurav.com")
#
# submit = driver.find_element_by_css_selector("form button")
# submit.click()



# at1=[]
# at2=[]
# at3=[]
# at4=[]
# at5=[]
# at6=[]
#
# att1=driver.find_elements_by_class_name("nb__2CMjv")
# for i in att1:
#     print(i.text)
#     at1.append(i.text)
#
# print(type(att1))
#
# att2=driver.find_elements_by_class_name("nb__3oNyC")
# for i in att2:
#     print(i.text)
#     at2.append(i.text)
#
#
# att3=driver.find_elements_by_id("roomType")
# for i in att3:
#     print(i.text)
#     at3.append(i.text)
#
#
# att4=driver.find_elements_by_class_name("nb__1nhEF")
# for i in att4:
#     print(i.text)
#     at4.append(i.text)
#
#
# att5=driver.find_elements_by_class_name("nb__fQJTh")
# for i in att5:
#     print(i.text)
#     at5.append(i.text)
#
#
# att6=driver.find_elements_by_class_name("nb__3FrOi")
# for i in att6:
#     print(i.text)
#     at6.append(i.text)


