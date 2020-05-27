from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def slow_typing(id, value):
    element = browser.find_element_by_id(id)
    element.send_keys(value)
    time.sleep(0.5)

options = webdriver.ChromeOptions()\
                    .add_argument("--user-data-dir='C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data\\Default'")

browser = webdriver.Chrome(chrome_options=options)

browser.get('https://www.browserstack.com')
print('title is:' , browser.title)
time.sleep(2)

cookie_cta = browser.find_element_by_id('accept-cookie-notification')
cookie_cta.click()

#<a href="/users/sign_up" id="signupModalButton" class="btn-primary btn-lg col-md-3 get-started-hero">Get started free</a>

button = browser.find_element_by_id('signupModalButton')
button.click()
time.sleep(2)

slow_typing('user_full_name', 'Rahul Verma')

slow_typing('user_email_login', 'rahul.hovs@gmail.com')

slow_typing('user_password', 'rahul1234')

time.sleep(1)

toc = browser.find_element_by_name('terms_and_conditions')
toc.click()

signupbutton = browser.find_element_by_id('user_submit')
signupbutton.click()

time.sleep(5)


#C:\Users\dell\AppData\Local\Google\Chrome\User Data\Default