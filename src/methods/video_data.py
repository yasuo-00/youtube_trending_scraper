from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

#return list of videos
def get_video_data( scraper):
    #get all videos data on page
    videos = scraper.find_elements_by_xpath('//*[@id="dismissible"]')
    video_list=[]
    for video in videos:
            
            curr_video = video.find_element_by_xpath('.//*[@id="video-title"]')
            scraper.execute_script('arguments[0].scrollIntoView(true)', curr_video)
            title = curr_video.text
            if(title!=''):
                #check if there is a description
                try:
                    description = WebDriverWait(video, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, './/*[@id="description-text"]'))).text
                except TimeoutException:
                    description=''               
                channel_name =video.find_element_by_xpath('.//*[@id="text"]').text 
                link = video.find_element_by_xpath('.//*[@id="video-title"]').get_attribute('href')
                views, posted_at= video.find_element_by_xpath('.//*[@id="metadata-line"]').text.split('\n')
                try:
                    video_duration = WebDriverWait(video, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, './/span[@class="style-scope ytd-thumbnail-overlay-time-status-renderer"]'))).text
                    #(By.XPATH, './/ytd-thumbnail-overlay-time-status-renderer[@class="style-scope ytd-thumbnail"]'))).text
                except TimeoutException:
                    video_duration=''
                    print("FAILED")             


                views = views.split(' ')[0]
                #transform scraped data into a dict
                videoData = {
                    'title': title,
                    'channel': channel_name, 
                    'views': views, 
                    'posted_at':posted_at,
                    'duration': video_duration,
                    'link': link,
                    'description': description 
                }
                #check for duplicates
                if videoData not in video_list:
                    #put videoData into a list
                    video_list.append(videoData)
    return video_list
