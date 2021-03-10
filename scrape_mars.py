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
    time.sleep(3)
    html = browser.html
    soup = bs(html,'html.parser')
    slides = soup.find_all('li', class_='slide')

    content_title = slides[1].find('div', class_ = 'content_title')
    news_title = content_title.text.strip()
    article_teaser_body = slides[1].find('div', class_ = 'article_teaser_body')
    news_p = article_teaser_body.text.strip()

    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p

    return mars_info

    browser.quit