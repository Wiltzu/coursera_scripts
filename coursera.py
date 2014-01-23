import os, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BROWSER = None
LOGIN_URL = 'https://accounts.coursera.org/signin'
CLASS_BASE_URL = 'https://class.coursera.org/'
VIDEO_DOWN_URL = '/lecture/download.mp4?lecture_id='

def authenticate(email, password):
    BROWSER.get(LOGIN_URL)
    BROWSER.find_element_by_css_selector('#signin-email').send_keys(email)
    BROWER.find_element_by_css_selector('#signin-password').send_keys(password + Keys.ENTER)

def download_video(course_name, video_id):
    video_url = CLASS_BASE_URL + course_name + VIDEO_DOWN_URL + video_id
    BROWSER.get(video_url)

def create_browser(courser_name):
    download_dir = os.getcwd() + course_name
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir", download_dir)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "video/mp4")
    #create download dir if not exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    return webdriver.Firefox(firefox_profile=fp)
    
    

if __name__ == '__main__':
    #get parameters
    email, password, course_name,last_video_id = [sys.argv[i] for i in range(1,5)]
    print email, password, course_name, last_video_id
    
    BROWSER = create_browser(course_name)
    authenticate(email,password)
    
    for video_id in range(last_video_id):
        download_video(course_name, video_id)

    BROWSER.quit()


