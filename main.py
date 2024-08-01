from driver import driver
from utils import group_link_selector, groups_url, log, linkedin_base_url, wait
from selenium.webdriver.common.by import By
from modules.login import login_to_LinkedIn

if __name__ == "__main__":

    driver.get(linkedin_base_url)

    # Checks if already logged in. If not then logins again
    if 'linkedin.com/feed' not in driver.current_url:
        login_to_LinkedIn()
        log('Login Successfull')
    else:
        log("User already Logged In. No need to log In")
    
    wait()
    driver.get(groups_url)
    log('Opened groups page')

    group_anchor_tags = driver.find_elements(By.CSS_SELECTOR, group_link_selector)
    log(f'found {len(group_anchor_tags)} groups')

    group_links = [ {'name' : a.text, 'link' : a.get_attribute("href")} for a in group_anchor_tags ]
    print(group_links)
    log('Program finished')