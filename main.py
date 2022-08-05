from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import time
import random
import os
email = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

load_dotenv()

PATH = r"E:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)

driver.get("http://159.89.38.11/login")

driver.find_element(By.ID, 'email-1').send_keys(EMAIL)
driver.find_element(By.ID, 'password-1').send_keys(PASSWORD)
driver.find_element(By.ID, 'm_login_signin_submit').click()

time.sleep(5)

action = webdriver.ActionChains(driver)
driver.get("http://159.89.38.11/contact/manage")

driver.find_element(By.LINK_TEXT, 'Add Contact').click()                                           #TC001
try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Add Contact"))
    )
except:
    print('TC001 failed')

time.sleep(3)
driver.find_element(By.NAME, 'number').send_keys(Keys.TAB * 9)                                    #TC002
try:
    element.get_attribute('Enter your address')
except:
    print('TC002 failed')

try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "*"))                                #TC006
    )
except:
    print('TC006 failed')

driver.find_element(By.NAME, 'number').send_keys(Keys.ENTER)
try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'help-block'))                              #TC007
    )
except:
    print('TC007 failed')

y = random.randint(300, 500)
driver.find_element(By.CLASS_NAME, 'add-new-group').click()                                        #TC008
time.sleep(2)
driver.find_element(By.NAME, 'name').send_keys("new tag " + str(y), Keys.TAB, "new tag description")
driver.find_element(By.ID, 'submit-group').click()
try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, 'submit-group'))
    )
except:
    print('TC008 failed')

driver.refresh()                                                                                     #TC009
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME, 'add-new-group').click()
time.sleep(2)
driver.find_element(By.NAME, 'name').send_keys(Keys.TAB, "new tag description")
driver.find_element(By.ID, 'submit-group').click()
try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, 'submit-group'))
    )
except:
    print('TC009 failed')

driver.refresh()                                                                                    #TC010
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME, 'add-new-group').click()
time.sleep(2)
z = random.randint(101, 200)
driver.find_element(By.NAME, 'name').send_keys("new tag " + str(z))
driver.find_element(By.ID, 'submit-group').click()
try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, 'submit-group'))
    )
except:
    print('TC010 failed')

driver.refresh()                                                                                    #TC011
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME, 'add-new-group').click()
try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, 'submit-group'))
    )
except:
    print('TC011 failed')

driver.refresh()
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.ID, 'checkbox-4-03').click()                                                   #TC012
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'email').send_keys('test123213@gmail.com')
driver.find_element(By.NAME, 'first_name').send_keys('First Name')
driver.find_element(By.NAME, 'last_name').send_keys('Last Name')
driver.find_element(By.NAME, 'city').send_keys('City')
driver.find_element(By.NAME, 'state').send_keys('State')
driver.find_element(By.NAME, 'zip').send_keys('Zip')
driver.find_element(By.NAME, 'country').send_keys('Country')
driver.find_element(By.NAME, 'address').send_keys('Address', Keys.TAB, Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC012 failed')

time.sleep(3)                                                                                         #TC013
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.ID, 'checkbox-4-0141').click()
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'email').send_keys('test123213@gmail.com')
driver.find_element(By.NAME, 'first_name').send_keys('First Name')
driver.find_element(By.NAME, 'last_name').send_keys('Last Name')
driver.find_element(By.NAME, 'city').send_keys('City')
driver.find_element(By.NAME, 'state').send_keys('State')
driver.find_element(By.NAME, 'zip').send_keys('Zip')
driver.find_element(By.NAME, 'country').send_keys('Country')
driver.find_element(By.NAME, 'address').send_keys('Address', Keys.TAB, Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC013 failed')

time.sleep(3)                                                                                          #TC014
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.ID, 'checkbox-4-03').click()
driver.find_element(By.ID, 'checkbox-4-0141').click()
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'email').send_keys('test123213@gmail.com')
driver.find_element(By.NAME, 'first_name').send_keys('First Name')
driver.find_element(By.NAME, 'last_name').send_keys('Last Name')
driver.find_element(By.NAME, 'city').send_keys('City')
driver.find_element(By.NAME, 'state').send_keys('State')
driver.find_element(By.NAME, 'zip').send_keys('Zip')
driver.find_element(By.NAME, 'country').send_keys('Country')
driver.find_element(By.NAME, 'address').send_keys('Address', Keys.TAB, Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC014 failed')

time.sleep(3)                                                                                           #TC015
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.ID, 'checkbox-4-03').click()
driver.find_element(By.NAME, 'number').send_keys(Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC015 failed')

driver.get("http://159.89.38.11/contact/manage")                                                     #TC016
time.sleep(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000), Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC016 failed')

time.sleep(3)                                                                                       #TC017
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(-10000, -1), Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog modal-lg"))
    )
except:
    print('TC017 failed')

driver.find_element(By.LINK_TEXT, 'Add Contact').click()                                            #TC018
driver.implicitly_wait(3)
q = driver.find_element(By.NAME, 'number')
q.send_keys('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','"','#','$','%','&','"','(',')','*',',','.','[','\\',']','^','_','{','}','|','~')

if q.get_attribute('value') is not None:
    print('TC018 failed')

driver.get("http://159.89.38.11/contact/manage")                                                    #TC020
x = random.randint(0, 100000)
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(x, Keys.ENTER)
driver.get("http://159.89.38.11/contact/manage")
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(x, Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC020 failed')

driver.get("http://159.89.38.11/contact/manage")                                                    #TC021
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'email').send_keys('test123213@gmail.com', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC021 failed')

driver.get("http://159.89.38.11/contact/manage")                                                    #TC022
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'email').send_keys('test123213', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog modal-lg"))
    )
except:
    print('TC022 failed')

driver.get("http://159.89.38.11/contact/manage")                                                  #TC023
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'email').send_keys('test123213@gmail.com', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog modal-lg"))
    )
except:
    print('TC023 failed')

driver.get("http://159.89.38.11/contact/manage")                                                  #TC024
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'first_name').send_keys('First Name', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC024 failed')

driver.get("http://159.89.38.11/contact/manage")                                                  #TC025
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'last_name').send_keys('Last Name', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC025 failed')

driver.get("http://159.89.38.11/contact/manage")                                                  #TC026
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'birthday').clear()
driver.find_element(By.NAME, 'birthday').send_keys('2023-07-15', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog modal-lg"))
    )
except:
    print('TC026 failed')

driver.get("http://159.89.38.11/contact/manage")                                                  #TC027
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'city').send_keys('City', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC027 failed')

driver.get("http://159.89.38.11/contact/manage")                                                   #TC028
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'state').send_keys('State', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC028 failed')

driver.get("http://159.89.38.11/contact/manage")                                                   #TC029
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'zip').send_keys('Zip', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC029 failed')

driver.get("http://159.89.38.11/contact/manage")                                                 #TC030
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'country').send_keys('Country', Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC030 failed')

driver.get("http://159.89.38.11/contact/manage")                                                    #TC031
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, 'Add Contact').click()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'number').send_keys(random.randint(0, 100000))
driver.find_element(By.NAME, 'address').send_keys('Address', Keys.TAB, Keys.ENTER)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col"))
    )
except:
    print('TC031 failed')

driver.quit()