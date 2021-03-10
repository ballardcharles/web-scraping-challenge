# Import Dependencies
import numpy as np
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import re
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return = Browser('chrome', **executable_path, headless=False)

mars_info = {}

def scrape_mars_news():

    # Initialize browser
    browser = init_browser()

    # Visit Mars news through splinter 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # slow scrape to allow to parse
    time.sleep(3)

    # HTML object
    html = browser.html

    # Parse with beautiful soup
    soup = bs(html,'html.parser')
    slides = soup.find_all('li', class_='slide')

    # Retrieve article titles and paragraph information
    content_title = slides[1].find('div', class_ = 'content_title')
    news_title = content_title.text.strip()
    article_teaser_body = slides[1].find('div', class_ = 'article_teaser_body')
    news_p = article_teaser_body.text.strip()

    # Add to dictionary
    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p

    return mars_info

    browser.quit

def scrape_mars_images():

    # Initialize browser
    browser = init_browser()

    # Visit Mars images through splinter 
    base_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"
    jpl_url = base_url + "index.html"
    browser.visit(jpl_url)

    # slow scrape to allow to parse
    time.sleep(3)

    # HTML object
    html = browser.html

    # Parse with beautiful soup
    soup = bs(html,'html.parser')

    # Retrieve image url information
    image_url = soup.find('a', class_='showimg fancybox-thumbs')['href']
    featured_image_url = base_url + image_url

    # Add to dictionary
    mars_info['image_url'] = featured_image_url

    return mars_info

    browser.quit

def scrape_mars_facts():

     # Initialize browser
    browser = init_browser()

    # Visit Mars facts through splinter 
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)

    # read mars fact table and place in variable
    mars_facts_table = pd.read_html(mars_facts_url)

    # Put mars fact table into pandas and clean data
    mars_df = mars_facts_table[0]
    mars_df = mars_df.rename(columns={0:'Fact', 1:'Value'})
    mars_df = mars_df
    mars_df['Fact'] = mars_df['Fact'].str.replace(':','')
    mars_df

    # Put Mars facts table into HTML
    mars_facts_html = mars_df.to_html(table_id="html_tbl_css",justify='left',index=False)

    # Add to dictionary
    mars_info['mars_tables'] = mars_facts_html

    return mars_info

    browser.quit

def scrape_mars_hemi():

    # Initialize browser
    browser = init_browser()

    # Visit hemi website through splinter
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

    # Parse hemi information
    html = browser.html
    soup = bs(html, 'html.parser')

    # Retrieve all items that have hemi info
    hemi_items = soup.find_all('div', class_='item')

    # Create empty list to house hemi information
    hemi_image_urls = []

    # Loop through items to pull title and image urls
    for item in hemi_items:
        
        title = item.find('h3').text
        
        partial_url = item.find('a', class_='itemLink product-item')['href']
        
        browser.visit(hemi_base_url + partial_url)
        
        html = browser.html
        
        soup = bs(html, 'html.parser')
        
        image_url = hemi_base_url + soup.find('img', class_='wide-image')['src']
        
        hemi_image_urls.append({"title": title, "img_url": image_url})

    mars_info['hemi_image_urls'] = hemi_image_urls

    return mars_info

    browser.quit()