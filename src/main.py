import sys, os
import pandas as pd
import time

from dotenv import load_dotenv
from utils import check_arguments
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from sort import sort
from methods import video_data

YTB_TRENDING_BASE_URL='https://www.youtube.com/feed/trending' #?persist_gl=1&gl=JP'

def main(argv):
    #load environment variables from file
    load_dotenv()
    if check_arguments.check_arguments(argv):
        output_directory = argv[1]

        #create directory if it doesn't exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        geckodriver_location = os.getenv('geckodriver_location') 
        options = Options()

        #set options
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--headless")
        scraper=webdriver.Firefox(options=options, executable_path=geckodriver_location)
        
        #get page
        #print(YTB_TRENDING_BASE_URL+ '?persist_gl=1gl&=JP')
        scraper.get(YTB_TRENDING_BASE_URL)
        scraper.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        scraper.save_screenshot('screenshot.png')
        #output_file = open(output_directory+"/output.txt", 'w')

        #output_file.write(scraper.page_source)
        video_list = video_data.get_video_data( scraper)
        
        
        df = pd.DataFrame(video_list) 
        #df = sort.sortByVideoTitle(True, df)
        #df = sort.sortByView(False, df)
        #df = sort.sortByTime(True,df)
        df.to_csv('output.csv', index=True)
        scraper.close()  



if __name__ == "__main__":
    main(sys.argv)
