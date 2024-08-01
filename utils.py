from selenium.webdriver.common.by import By
from credentials import username, password
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier

toaster = ToastNotifier()
def notify(msg : str, duration : int = 3):
	toaster.show_toast(title='LinkedIn Script', msg=msg, duration=duration)

log_file_name = 'logs.txt'
# reseting logs
with open(log_file_name, 'wt') as file:
	pass
def log(msg : str):
	notify(msg)
	print(f'\n{msg}\n')
	with open(log_file_name, 'at') as log_file:
		log_file.write(f'{msg}\n')

def wait(time : float = 5):
	log(f'Waiting for {time} Seconds...')
	sleep(time)

# links
login_url = "https://www.linkedin.com/login"
groups_url = "https://www.linkedin.com/groups/"
linkedin_base_url = "https://www.linkedin.com"

# selctors
group_link_selector = 'li.artdeco-list__item div.artdeco-entity-lockup__content.ember-view a'