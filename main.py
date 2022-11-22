from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv("./.env")



chrome_driver_path = "/Users/tinalee/Documents/dev/chromedriver"

service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

search_url = "https://www.linkedin.com/jobs/search/"
driver.get(search_url)
time.sleep(5)
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

username = driver.find_element(By.NAME, "session_key")
username.send_keys("suckerforpez@gmail.com")

password = driver.find_element(By.NAME, "session_password")
password.send_keys(os.getenv("LINKEDIN_PASSWORD"))

sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in_button.click()

search_box = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
search_box.send_keys("python developer")

search_button = driver.find_element(By.CLASS_NAME, "jobs-search-box__submit-button")
search_button.click()
time.sleep(5)
easy_apply_filter = driver.find_element(By.CLASS_NAME, "search-reusables__filter-binary-toggle")
easy_apply_filter.click()
time.sleep(5)

jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
for job in jobs:
    job.click()
    time.sleep(3)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    if save_button.text.split('\n')[0] == "Save":
        save_button.click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "artdeco-toast-item__dismiss").click()
    else:
        time.sleep(3)

time.sleep(200)