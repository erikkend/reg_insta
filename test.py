from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'./chromedriver')
driver.get("https://www.instagram.com/accounts/emailsignup/")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='emailOrPhone']"))).send_keys("9876543210")
driver.find_element_by_xpath("//input[@name='fullName']").send_keys("aforkman")
driver.find_element_by_xpath("//input[@name='username']").send_keys("aforkman")
driver.find_element_by_xpath("//input[@name='password']").send_keys("aforkman")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Регистрация']"))).click()
