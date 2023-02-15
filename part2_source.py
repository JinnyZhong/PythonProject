#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


# In[ ]:


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


# In[ ]:


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
    print("The latest:", hours, ":", mins, ":", seconds)
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


# In[ ]:


main2a()


# In[ ]:


main2b() 

