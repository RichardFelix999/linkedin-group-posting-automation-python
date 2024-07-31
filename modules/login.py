from driver import driver
from selenium.webdriver.common.by import By
from utils import wait, log, login_url, groups_url
from credentials import username, password
import easygui

def login_to_LinkedIn():
	log('Attepting to Log In...')
	driver.get(login_url)
	driver.find_element(By.ID, "username").send_keys(username)
	driver.find_element(By.ID, "password").send_keys(password)
	wait()
	driver.find_element(By.CSS_SELECTOR, "div.login__form_action_container > button").click()
	log('Submitted Login form')
	while True:
		wait()
		if ".com/checkpoint/challenge" in driver.current_url:
			log('Asking for Captcha verification')
			easygui.msgbox(title='LinkedIn Script', msg='Please perform captcha verification you have 20 seconds to complete it')
			driver.get(groups_url)
		else:
			log('No Captcha Asked')
			driver.get(groups_url)
			break