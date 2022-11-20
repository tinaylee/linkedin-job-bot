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

search_url = "https://www.linkedin.com/jobs/search/?currentJobId=3256750813&f_E=2&f_JT=F&geoId=104116203&keywords=python" \
             "%20software%20engineer&location=Seattle%2C%20Washington%2C%20United%20States&refresh=true&start=50"
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
time.sleep(1000)