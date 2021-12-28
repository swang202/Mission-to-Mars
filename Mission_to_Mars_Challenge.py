#!/usr/bin/env python
# coding: utf-8

# In[65]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[66]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[67]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button, searched <button only 3 showed up
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


import pandas as pd
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df


# In[ ]:


df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# In[6]:


browser.quit()


# # Challenge Starter Code

# In[7]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[8]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[34]:


# Visit the mars nasa news site
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[35]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.result-list')


# In[38]:


slide_elem.find('div', class_='description')


# In[33]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('h3').get_text()
news_title


# In[13]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('p').get_text()
news_p


# ### JPL Space Images Featured Image

# In[39]:


# Visit URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[40]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('img.thumb')[0]
full_image_elem.click()


# In[41]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[49]:


title = img_soup.find('h2', class_='title').get_text()
title


# In[45]:


img_soup_ele=img_soup.find('div', class_='downloads')
img_soup_ele


# In[27]:


# find the relative image url
img_url = img_soup_ele.find('a').get('href')
img_url


# In[7]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


hemispheres_image_urls = []

for var in range(4):
    
    hemispheres={}

    full_image_elem = browser.find_by_tag('img.thumb')[var]
    full_image_elem.click()

    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # find title
    title = img_soup.find('h2', class_='title').get_text()
    
    # find the image url
    img_soup_ele=img_soup.find('div', class_='downloads')
    img_url = img_soup_ele.find('a').get('href')

    # assign to list
    hemispheres['title'] = title
    hemispheres['img_url'] = img_url
    hemispheres_image_urls.append(hemispheres)

    # Browse back to repeat
    browser.back()

browser.quit()

hemispheres_image_urls


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[ ]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[ ]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.


# In[ ]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[6]:


# 5. Quit the browser
browser.quit()


# In[ ]:




