import sys, os
import pandas as pd
import time
from dotenv import load_dotenv
from utils import check_arguments
from classes.scraper import Scraper
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from sort import sort



def main(argv):
    load_dotenv()
    if check_arguments.check_arguments(argv):
        output_directory = argv[1]

        #create directory if it doesn't exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        geckodriver_location = os.getenv('geckodriver_location')
        options = Options()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--headless")
        scraper=webdriver.Firefox(options=options, executable_path=geckodriver_location)
        scraper.get('https://www.youtube.com/feed/trending')
        output_file = open(output_directory+"/output.txt", 'w')
        '''
        try:
            videos = WebDriverWait(scraper, 10).until(EC.presence_of_element_located((By.ID,'//*[@id="description-text"]')))
        except TimeoutException:
            scraper.get_screenshot_as_file("screenshot.png")
            print("Timed out")
        '''
        videos = scraper.find_elements_by_xpath('//*[@id="dismissible"]')
        output_file.write(scraper.page_source)
        video_list = []
        
        for video in videos:
            
            title = video.find_element_by_xpath('.//*[@id="video-title"]').text
            if(title!=''):
                #check if there is a description
                try:
                    description = WebDriverWait(video, 5).until(EC.element_to_be_clickable(
                    (By.XPATH, './/*[@id="description-text"]'))).text
                except TimeoutException:
                    description=''               
                channel_name =video.find_element_by_xpath('.//*[@id="text"]').text 
                link = video.find_element_by_xpath('.//*[@id="video-title"]').get_attribute('href')
                views, posted_at= video.find_element_by_xpath('.//*[@id="metadata-line"]').text.split('\n')
                #print(title)
                #print(views_posted_time.splitlines())
                '''
                time_duration = description = WebDriverWait(video, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span'))).text
                '''
                print(time_duration)
                views = views.split(' ')[0]
                #print(views)
                videoData = {
                    'title': title, 
                    'views': views,
                    'posted_at':posted_at,
                    'channel': channel_name,
                    'link': link,
                    'description': description 
                }
                if videoData not in video_list:
                    video_list.append(videoData)
        
        df = pd.DataFrame(video_list) 
        #df = sort.sortByVideoTitle(True, df)
        #df = sort.sortByView(True, df)
        df.to_csv(output_directory+'/output.csv', index=True)
        print('FIM')
        output_file.close() 
        scraper.close()  



if __name__ == "__main__":
    main(sys.argv)
