#!/usr/bin/env python
# coding: utf-8

# In[15]:


from bs4 import BeautifulSoup
import requests
import time


# # Part I

# In[17]:


def main():
    URL = "https://www.planespotters.net/user/login"
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
    
    time.sleep(5)
    ## GET request. Read and store the cookies received in the response. 
    session_requests = requests.session()
    res = session_requests.get(URL, headers=header)
    # parse the response
    res_parse = BeautifulSoup(res.content, 'html.parser')
    cookies_get = session_requests.cookies.get_dict()
    # print(cookies_get)
    
    time.sleep(5)
    # read (and store to a string variable) the value of the hidden input field that will (most likely) be required in the login process
    input_csrf = res_parse.select("div.planespotters-form input[name=csrf]")[0]
    csrf = input_csrf.get("value")
    input_rid = res_parse.select("div.planespotters-form input[name=rid]")[0]
    rid = input_rid.get("value")
    # print(csrf, rid)
    
    ## (2) Make a POST request using the cookies from (1) and all required name-value-pairs
    # session_requests_post = requests.session()
    res_post = session_requests.post(URL, 
                                          data = {"username" : "",
                                          "password" : "", 
                                          "csrf" : str(csrf), 
                                          "rid" : ''},
                                          headers = header, cookies = cookies_get,
                                          timeout = 10)

    ## (3) Get the cookies from the response of the post request
    cookies_post = session_requests.cookies.get_dict()
    print("cookies_post:", cookies_post)

    # cookies_dict
    cookies_dict = str(cookies_get) + str(cookies_post)
    
    # (4) Verifies that you are logged in by accessing the profile page with the saved cookies
    time.sleep(5)
    url = 'https://www.planespotters.net/member/profile'
    page2 = session_requests.get(url, headers=header, cookies = cookies_post)
    profile = BeautifulSoup(page2.content,'html.parser')
    
    # (5)
    # print out the entire BeautifulSoup document of your profile page
    print(profile)

    # All (combined) cookies from (3)
    print(cookies_dict)

    # A boolean value to show your username is contained in the document in part (5)(a).
    # print(bool(profile.findAll(text = "jinny666")))
    


# In[18]:


main()


# # Part II

# In[19]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


# In[21]:


# Question 1
def main2a():
    driver = webdriver.Chrome(executable_path='/Users/zhongjinying/Downloads/chromedriver_mac64/chromedriver')
    driver.implicitly_wait(10)
    driver.set_script_timeout(120)
    driver.set_page_load_timeout(10)
    driver.get("https://google.com")
    inp = driver.find_element(By.CSS_SELECTOR, "input[type=text]")
    inp.send_keys("askew\n")
    time.sleep(5)
    # navigate back to home page
    driver.get("https://google.com")
    inp = driver.find_element(By.CSS_SELECTOR, "input[type=text]")
    inp.send_keys("google in 1998\n")
    driver.implicitly_wait(10)
    driver.set_script_timeout(120)
    driver.set_page_load_timeout(10)
    driver.quit()


# In[34]:


# Question 2
def main2b():
    driver = webdriver.Chrome(executable_path='/Users/zhongjinying/Downloads/chromedriver_mac64/chromedriver')
    driver.implicitly_wait(10)
    driver.set_script_timeout(120)
    driver.set_page_load_timeout(10)
    driver.get("https://www.bestbuy.com/")

    # click on Deal of the Day
    dealofday = driver.find_element(By.XPATH, "//a[text()='Deal of the Day']")
    dealofday.click()
    driver.set_page_load_timeout(20)
    time.sleep(5) 

    # read how much time is left for the Deal of the Day  'div.countdown-clock span'
    # print the remaining time to screen
    hours = driver.find_element(By.CSS_SELECTOR, "span[class ='hours cdnumber']")
    hours = hours.text
    mins = driver.find_element(By.CSS_SELECTOR, "span[class ='minutes cdnumber']")
    mins = mins.text
    seconds = driver.find_element(By.CSS_SELECTOR, "span[class ='seconds cdnumber']")
    seconds = seconds.text
    print(hours, ":", mins, ":", seconds)
    time.sleep(5) 

    # click on the actual product
    productlink = driver.find_element(By.XPATH, "//h1[@class='heading product-title']/a")
    productlink.click()
    driver.set_page_load_timeout(20)

    # click on its review
    review = driver.find_element(By.XPATH, "//span[text()='Reviews']")
    review.click()
    driver.set_page_load_timeout(20)

    # save the resulting HTML to your local hard drive
    with open("/Users/zhongjinying/Desktop/bestbuy_deal_of_the_day.htm", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    driver.quit()


# In[23]:


main2a()


# In[35]:


main2b()

