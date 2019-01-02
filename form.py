#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: mortezaghasemi
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


url = 'http://student1.iauyazd.ac.ir/mechanizeh/studentportal/'
driver = webdriver.Chrome('/home/mortezaghasemi/Downloads/CompleterArzyabi-master/chromedriver')
driver.maximize_window()
driver.get(url)
driver.find_element_by_id('txtUsername').send_keys("USERNAME")
driver.find_element_by_id('txtPassword').send_keys("PASSWORD ")
driver.find_element_by_id('txtCaptcha').send_keys("")

try:
    element = WebDriverWait(driver, 10).until(
        EC.url_changes('http://student1.iauyazd.ac.ir/mechanizeh/studentportal/')
    )

except Exception as e:
    raise Exception('Time End')

time.sleep(3)
print("LOGIN")
menu = driver.find_element_by_id('ctl00_Menu_Edu')
hidden_submenu = driver.find_element_by_css_selector("#ctl00_Mnu_Edu_Evaluation")
hidden_hidden_submenu = driver.find_element_by_id('ctl00_mnu_stu_services_eval')

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.move_to_element(hidden_submenu)
actions.click(hidden_hidden_submenu)
actions.perform()

# driver.quit()

# ctl00_ContentPlaceHolder1_Grd_Executer
buttons = driver.find_elements_by_xpath('//*[@style="color:#3399FF;text-decoration:none;"]')

ARROW_DOWN = u'\ue015'
buttons_len = len(buttons)

for n in range(buttons_len):
    butt = driver.find_element_by_xpath('//*[@style="color:#3399FF;text-decoration:none;"]')
    butt.click()
    time.sleep(1)
    selects = driver.find_elements_by_xpath('//select')
    for select in selects:
        print select
        select.send_keys(ARROW_DOWN)
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    time.sleep(1)
    driver.back()
