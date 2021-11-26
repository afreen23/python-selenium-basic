from pathlib import Path
import datetime
import logging
import os
import time
import zipfile

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
)
from time import sleep
from selenium.webdriver.remote.file_detector import UselessFileDetector

logger = logging.getLogger(__name__)


browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.file_detector = UselessFileDetector()
browser.get('http://localhost:9000/k8s/cluster/storageclasses/~new/form')
sleep(15)

# select provisioner
provisioner = browser.find_element(By.ID,'storage-class-provisioner')
provisioner.send_keys(Keys.ENTER)


#  select search input
searchInput = browser.find_element(By.CSS_SELECTOR, 'input[data-test-id="dropdown-text-filter"]')
provisioner.send_keys('openshift-storage.rbd.csi.ceph.com')

# select rbd
option = browser.find_element(By.ID,'openshift-storage.rbd.csi.ceph.com-link')
option.send_keys(Keys.ENTER)

sleep(5)

# click enable encryption
browser.find_element(By.CSS_SELECTOR, 'input[data-test="storage-class-encryption"]').click()

sleep(5)

# click advanced settings
browser.find_element(By.ID,  'create-new-kms-connection').click()

sleep(5)

browser.find_element(By.CSS_SELECTOR, 'button[data-test="kms-advanced-settings-link"]').click()

sleep(5)


# click .pem file
file_input = browser.find_element(By.XPATH, '//*[@id="modal-container"]/div/div/div/form/div/div[2]/div/div/div[4]/div[2]/div/input')
file_input.send_keys('/home/wiz/workspace/python-selenium-basic/dummy.pem')

file_input = browser.find_element(By.XPATH, '//*[@id="modal-container"]/div/div/div/form/div/div[2]/div/div/div[5]/div[2]/div/input')
file_input.send_keys('/home/wiz/workspace/python-selenium-basic/dummy.pem')


file_input = browser.find_element(By.XPATH, '//*[@id="modal-container"]/div/div/div/form/div/div[2]/div/div/div[6]/div[2]/div/input')
file_input.send_keys('/home/wiz/workspace/python-selenium-basic/dummy.pem')

sleep(10)


browser.quit()



