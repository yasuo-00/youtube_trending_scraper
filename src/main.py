import sys, os
import pandas as pd
import time
import argparse

from dotenv import load_dotenv
from utils import check_arguments
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from sort import sort
from methods import video_data

YTB_TRENDING_BASE_URL='https://www.youtube.com/feed/trending' #?persist_gl=1&gl=JP'

parser = argparse.ArgumentParser(description='Youtube Trending Viedos Scraper')
parser.add_argument('-od', '--output-directory', type=str, metavar='output_directory', help='Output Directory Path')
parser.add_argument('-f', '--filename', type=str, metavar='filename', help='Output File Name')
parser.add_argument('-l','--location', type=str, metavar='location', help='Specify From Which Country to Scrap Videos')
group = parser.add_mutually_exclusive_group()
group.add_argument('--date', action='store_true', help='Sort By Date')
group.add_argument('--duration', action='store_true', help='Sort By Video Duration')
group.add_argument('--alpha', action='store_true', help='Sort By Video Name')
group.add_argument('--views', action='store_true', help='Sort By Views')
parser.add_argument('-d', '--descending', action='store_true', help='Sort In Descending Order')
args= parser.parse_args()


def main(args):

    
    #load environment variables from file
    load_dotenv()

    geckodriver_location = os.getenv('geckodriver_location') 
    options = Options()

    #set options
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--headless")
    scraper=webdriver.Firefox(options=options, executable_path=geckodriver_location)
    
    #get page
    #(YTB_TRENDING_BASE_URL+ '?persist_gl=1gl&=JP')
    url =YTB_TRENDING_BASE_URL
    if args.location is not None:
        url=YTB_TRENDING_BASE_URL+'?persist_gl=1&gl='+args.location
        print(url)
    scraper.get(url)
    #output_file = open(output_directory+"/output.txt", 'w')

    #output_file.write(scraper.page_source)
    video_list = video_data.get_video_data( scraper)
    
    
    df = pd.DataFrame(video_list) 

    if args.alpha:
        df = sort.sortByVideoTitle(args.ascending, df)
    elif args.views:
        df = sort.sortByView(args.ascending, df)
    elif args.duration:
        df = sort.sortByTime(args.ascending,df)

    if args.output_directory is not None:
        #create directory if it doesn't exists
        if not os.path.exists(args.output_directory):
            os.makedirs(args.output_directory)
        if args.filename is not None:
            df.to_csv(args.output_directory+'/'+args.filename, index=True)
        else:
            df.to_csv(args.output_directory+'/'+'output.csv', index=True)
    else:
        if args.filename is not None:
            df.to_csv(args.filename+'.csv', index=True)
        else:
            df.to_csv('output.csv', index=True)
    
    scraper.close()  



if __name__ == "__main__":
    main(args)
