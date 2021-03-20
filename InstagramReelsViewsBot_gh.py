# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 01:06:53 2021

@author: VICKY JUNGHARE
"""
#importing required python packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
import time
import random

username= "Dummy" #Instagram Username
password= "Dummy@123" #Instagram Password

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.instagram.com/")
enter_username = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'username')))
enter_username.send_keys(username)
   
enter_password = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'password')))
enter_password.send_keys(password)
enter_password.send_keys(Keys.RETURN)
time.sleep(random.randint(1,4))

try:
  	not_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
  	a= not_now.find_elements_by_tag_name("button")[1]
  	actions = ActionChains(driver)
  	actions.click(a)
  	actions.perform()
except:
   	pass
   
finally:
	for i in range(500): #Number of views
            driver.get("https://www.instagram.com/reel/CKyg3-7hGiE/") #Reel link
            time.sleep(random.randint(1,2))