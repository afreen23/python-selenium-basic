from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('http://www.google.com')
sleep(5)
browser.quit()