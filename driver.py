from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from time import sleep
from shutil import copytree
from utils import log
from selenium import webdriver

base_path = os.getcwd()
profile_path_original = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default')
profile_path_local = os.path.join(base_path, 'profile')
driver_path = os.path.join(base_path, 'webdrivers', 'chromedriver.exe')

def create_profile():
    log(f'Copying files from {profile_path_original}')
    copytree(profile_path_original, profile_path_local)
    log('Successfully copied profile')

# creating profile:
if not os.path.exists(profile_path_local):
    log('Unable to find profile. Creating default profile')
    # os.mkdir(profile_path_local)
    create_profile()
else:
    log('Found profile in root directory')

options = Options()

# using headless driver mode. Comment or uncomment based on your need
# options.add_argument("--headless")

# using default profile
options.add_argument(f"--user-data-dir={profile_path_local}")

driver = Chrome(service=Service(executable_path=driver_path), options=options)

if __name__ == "__main__":
    print(profile_path_local)