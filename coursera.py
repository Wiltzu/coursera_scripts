#!/usr/bin/env python

import os, sys, time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BROWSER = None
LOGIN_URL = 'https://accounts.coursera.org/signin'
CLASS_BASE_URL = 'https://class.coursera.org/'
VIDEO_DOWN_URL = '/lecture/download.mp4?lecture_id='

def authenticate(email, password):
    BROWSER.get(LOGIN_URL)
    #TODO: wait until following elements are visible
    time.sleep(1)
    BROWSER.find_element_by_css_selector('input#signin-email').send_keys(email)
    BROWSER.find_element_by_css_selector('input#signin-password').send_keys(password + Keys.ENTER)
    #wait until some element is visible
    time.sleep(5)

def download_video(course_name, video_id):
    #TODO: go to video page and actually click links to make sure that every video is downloaded
    video_url = CLASS_BASE_URL + course_name + VIDEO_DOWN_URL + str(video_id)
    print "downloading video from url: " + video_url
    BROWSER.get(video_url)
    #TODO: wait until there is no .part file in the download directory
    time.sleep(5)

def create_browser(courser_name):
    download_dir = os.path.join(os.getcwd(), course_name)
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
    email, course_name,first_video_id, last_video_id = [sys.argv[i] for i in range(1,5)]
    password = getpass.getpass()
    print email, course_name, last_video_id
    
    BROWSER = create_browser(course_name)
    authenticate(email,password)
    if(BROWSER.current_url == 'https://www.coursera.org/'):
        for video_id in range(int(first_video_id), int(last_video_id) + 1):
            download_video(course_name, video_id)
    else:
        print "authentication failed. url was: " + BROWSER.current_url
        #more error handling!!
    #TODO: sign out and close browser when all downloads are complete
    #BROWSER.quit()


