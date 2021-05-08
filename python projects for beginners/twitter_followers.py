"""
This application takes the followers from the Twitter account. Creates a text document and save the followers.
Given sort sleep times for page load.
"""

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "https://twitter.com/login" # entering the login page of twitter
browser = webdriver.Chrome() # browser set as chrome
browser.get(url) # open the browser and go the url
time.sleep(2)

action = webdriver.ActionChains(browser) # creating an action wariable for pressing some keys

# at this lines code enters the username and password to target boxes and click (send) enter key.
username_box = browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input""")
username_box.send_keys("sample_username")
password_box = browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input""")
password_box.send_keys("sample_password")
password_box.send_keys(Keys.ENTER)
time.sleep(1)


# getting profile page
browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/a""").click()
time.sleep(1)

# Taking the number of followers
followers_count = browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span""").text
# getting followers page
browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a""").click()
time.sleep(1)



with open("Twitter_followers.text","a+",encoding="UTF-8") as file: # Creaing a text document for save followers.

    names_list = [] # Creating a empty list for appending followers

    while int(followers_count) > len(names_list) : # a while loop that controls the followers number and list_len

        followers_list = browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div""").find_elements_by_css_selector(".css-901oao.css-bfa6kz.r-1fmj7o5.r-1qd0xha.r-a023e6.r-b88u0q.r-rjixqe.r-bcqeeo.r-1udh08x.r-3s2u2q.r-qvutc0")
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform() # press space key for load next followers that unloaded

        for a in followers_list: 
            if a not in names_list: # append the follower if its not already in the list
                file.write(f"{a}\n")
                

        time.sleep(1)

