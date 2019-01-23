from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()



driver.get("https://slack.com/signin") #This is the website that will launch
try:
	#domain = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "domain")))
	domain = driver.find_element_by_id('domain')
	domain.clear()
	domain.send_keys("test-60t7981.slack.com")

	signin = driver.find_element_by_id("submit_team_domain")
	signin.click()

	email = driver.find_element_by_id('email')
	password = driver.find_element_by_id('password')

	email.clear()
	password.clear()

	email.send_keys("bloodypikachu@gmail.com")
	password.send_keys('qatest123')

	signinlogin = driver.find_element_by_id("signin_btn")
	signinlogin.click()

	msgbox = driver.find_element_by_xpath('//*[@id="msg_input"]/div[1]')
	msgbox.click()
	msgbox.send_keys("Hello peoples")
	msgbox.send_keys(Keys.ENTER)


finally:
	print("fail")