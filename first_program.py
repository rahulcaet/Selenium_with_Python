
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://www.python.org")
print(driver.title)

'''
 <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

'''

#search_bar = driver.find_element_by_name("q")

#search_bar = driver.find_element_by_id("id-search-field")

#search_bar  = driver.find_element_by_class_name("search-field")

search_bar  = driver.find_element_by_xpath("//input[@id='id-search-field']")

search_bar.clear()

search_bar.send_keys("getting started with python")

search_bar.send_keys(Keys.RETURN)

print(driver.current_url)

driver.close()