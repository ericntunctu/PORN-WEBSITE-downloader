#!/usr/bin/env python
# coding: utf-8

# In[9]:


import urllib
from selenium import webdriver
import urllib.request
import time
import re
import urllib
from selenium.webdriver.common.keys import Keys
from PIL import *
import PIL.Image as img



def comicsdownload(url, pages):  
    driver = webdriver.Chrome(executable_path="/Users/kuoenjui/Desktop/scraper/chromedriver") # choose the  webdriver location (chrome)
    driver.get(url)  # comics url
    driver.find_element_by_xpath('//*[@id="gdt"]/div[1]/div/a/img').click()  
    for i in range(0, pages):  # how many pages
        img = driver.find_element_by_xpath('//*[@id="img"]').get_attribute('src')
        urllib.request.urlretrieve(img, "0000000"+str(i)+".jpg")
        driver.find_element_by_xpath('//*[@id="next"]/img').click()
        time.sleep(0.8)

        
text1=input('your url (number) ex:g/1218702/6570f61212/: ')
text2=input('download pages: ')
        
comicsdownload("https://e-hentai.org/"+text1, int(text2))  # it will download for you.


# In[10]:





# In[ ]:




