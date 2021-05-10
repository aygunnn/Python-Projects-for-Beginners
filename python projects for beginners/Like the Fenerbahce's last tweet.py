"""
This application will like the lastest tweet of the Official Fenerbahçe Account in Twitter
using Selenium and chrome webdriver. Given short sleep times for the page load.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # Open webdriver by the chrome.
url = "https://twitter.com/login" 
driver.get(url) # open the target url
driver.maximize_window()
time.sleep(1)

username = driver.find_element_by_name("session[username_or_email]") # selecting username_box
username.send_keys("sample_username") # sending the keys "username" to the username_box

password = driver.find_element_by_name("session[password]") # selecting the password_box
password.send_keys("sample_password") # sending the keys "password" to the password_box
password.send_keys(Keys.ENTER) # send keys enter. that means press enter at the password_box
time.sleep(3)

# Click the search_box
search = driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input""")
search.send_keys("Fenerbahçe") # send "Fenerbahce" keys to search_box
search.send_keys(Keys.ENTER) # send enter key
time.sleep(3)

# Search the official account of Fenerbahce
fenerbahce = driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/span""")
fenerbahce.click() # Click the given path
time.sleep(3)

# Enterin the official accounts page.
offical_page = driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/div/div[2]/div[1]""")
offical_page.click()
time.sleep(3)

# Find the newest tweet at this page
tweet = driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div""")
tweet.click() # Click the tweet
time.sleep(1)

# Find the like button by given path
like = driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div[3]/div/div/div""")
like.click() # Click the like button
time.sleep(5)

driver.close() # Close the Webdriver
