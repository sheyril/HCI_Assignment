import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


# options = webdriver.chrome.options.Options()
# options.add_argument('--log-level=3')  
# options.add_argument('--headless')
# Desired

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome("/Users/sheyril/Desktop/HCI/chromedriver", options=options)

# driver = webdriver.Chrome("/Users/sheyril/Desktop/HCI/chromedriver")#create an object driver


# driver = webdriver.Chrome(options=options)
driver.implicitly_wait = 1

driver.maximize_window() # maximise the window.
driver.get("https://www.isro.gov.in/") # open a link.
# driver.find_element_by_class_name("close").click()
# content.click()

do_not_validate = (
    'javascript:',
    'mailto:',
    'tel:',
)

links = driver.find_elements_by_css_selector("a")


for link in links:
    temp = link.get_attribute('href')
    print(temp)
    if (temp and not temp.startswith(do_not_validate)):
        if (requests.head(link.get_attribute('href')).status_code == 200):
            print(link.get_attribute('href') + " is valid")
        else:
            print(link.get_attribute('href') + " is broken")





# search_bar = driver.find_element_by_name("q") # find element by tag (here name="q").
# search_bar.send_keys("bits hyderabad") #send keys to search bar.
# search_bar.send_keys(Keys.RETURN) # Enter to search.

# link = driver.find_element_by_link_text("BITS Campuses")#find element by link_text.
# link.click() # click. 
# time.sleep(3) #ask selenium to wait for 3 seconds.
# driver.execute_script("window.scrollTo(0, 850)") # scroll from 0 to Y. 

# You can find element by using any tag you wish.
# So find out yourself, which tag to use to open all the hyper links in the home page of the given 5 websites.
# Find out how to calculate the time taken by each link to load.




# not a v good practice, find alternative
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#For compatibility issues, we can download the correct webdriver version automatically using this
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
