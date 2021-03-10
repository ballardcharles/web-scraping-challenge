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

    # Visit Mars news through splinter 
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

    # Visit Mars news through splinter 
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)

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