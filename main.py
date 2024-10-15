import time

from selenium import webdriver
from dotenv import load_dotenv
import os
from InternetSpeedTwitterBot import InternetSpeedTwitterBot
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

load_dotenv()
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_service = Service("/Users/mac/Downloads/chromedriver-mac-arm64/chromedriver")


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

download_speed = 300
upload_speed = 200
internet_speed_libk = "https://www.speedtest.net/"
twitter_link = "https://twitter.com/i/flow/signup"
Twitter_email = os.getenv("USERNAME")
Twitter_password = os.getenv("PASSWORD")

driver.get('https://twitter.com/i/flow/signup')
