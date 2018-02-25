import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time_util import sleep
from selenium.common.exceptions import NoSuchElementException

# get login credentials
email = input(print('Enter email: '))
password = input(print('Enter password: '))

# get post url
post_url = input(print('Enter post url: '))

# create a new Chrome session
chromedriver_location = "./assets/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.maximize_window()

# log in
driver.get("https://www.facebook.com")
search_field = driver.find_element_by_id("email")
search_field.send_keys(email)
search_field = driver.find_element_by_id("pass")
search_field.send_keys(password)
search_field.submit()

print("Logged in as " + email)

# navigate to the post url
driver.get(post_url)
engagement_div = driver.find_element_by_css_selector("a[href*='/ufi/reaction']")
driver.execute_script("arguments[0].click();", engagement_div)

# switch to all engagement - not working
engagement_all = driver.find_element_by_css_selector("a[tabindex*='-1']")
driver.execute_script("arguments[0].click();", engagement_div)

# click see more until there no such option
print("Loading all the users.")

while True:
    try:
        viewMoreButton = driver.find_element_by_css_selector("a[href*='/ufi/reaction/profile/browser/fetch']")
        driver.execute_script("arguments[0].click();", viewMoreButton)
        sleep(2)
    except NoSuchElementException:
        break

# invite users
print("Inviting the users.")
users = driver.find_elements_by_css_selector("a[ajaxify*='/pages/post_like_invite/send/']")
invitedUsers = 0

for i in users:
    user = driver.find_element_by_css_selector("a[ajaxify*='/pages/post_like_invite/send/']")
    driver.execute_script("arguments[0].click();", user)
    invitedUsers = invitedUsers + 1
    sleep(1)

print('My job is done here. I have invited: ' + str(invitedUsers))

# close the browser window
driver.quit()