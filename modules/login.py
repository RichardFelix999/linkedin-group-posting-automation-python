from driver import driver
from selenium.webdriver.common.by import By
from utils import wait, log, login_url, groups_url
from credentials import username, password
import easygui
from selenium.common.exceptions import NoSuchElementException

welcome_back_selector = '#fastrack-div > div.header__content > h1'
signinwithanotherac_anchor_selector = '.signin-other-account a'

def login_to_LinkedIn():
	log('Attepting to Log In...')
	driver.get(login_url)
	try:
		driver.find_element(By.ID, "username").send_keys(username)
	except NoSuchElementException:
		log('Username input not found')
		try:
			signinwithanotherac_anchor = driver.find_element(By.CSS_SELECTOR, signinwithanotherac_anchor_selector)
			signinwithanotherac_anchor.click()
			log('Clicked on <Sign in with another Account>')
			wait(10)
			driver.find_element(By.ID, "username").send_keys(username)
		except NoSuchElementException:
			log('<Sign in with another Account> button not found')
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