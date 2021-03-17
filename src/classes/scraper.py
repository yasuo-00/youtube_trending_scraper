
import requests
import os
from selenium import webdriver

class Scraper():

    def __init__(self):
        self.__driver = webdriver.Firefox()
    
    def get_page_html(self, site_address):

        return self.__driver.get(site_address)


    def get_videos(self, page):
        
        return self.__driver.find_elements_by_xpath('//*[@id="dismissible"]')

    def get_video_title(self, video):

        return self.__driver.find_elements_by_xpath('//*[@id="video-title"]').text

    def get_video_duration(self, page):
        pass

    def get_video_views(self, page):
        pass
