# Import libraries and packages for the project 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import csv

print('importing finished')

driver=webdriver.Chrome(executable_path='E:\\selenium_webdriver\\chromedriver')
sleep(1)
url = 'https://www.linkedin.com/login'
driver.get(url)
print('Finished initializing a driver')
sleep(1)

# credential = open('credentials.txt')
# line = credential.readlines()
# username = line[0]
# password = line[1]
username='hrudayesh22@gmail.com'
password='Kingnani@22'
print('Finished importing the login credentials')
sleep(1)

email_field = driver.find_element_by_id('username')
email_field.send_keys(username)
sleep(1)

password_field = driver.find_element_by_name('session_password')
password_field.send_keys(password)
sleep(1)

# Login button
# signin_field = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
signin_field=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
signin_field.click()
sleep(1)

print('finised Login to Linkedin')

# search_field=driver.find_element_by_xpath('/html/body/div[5]/header/div/div/div/button/li-icon/svg')
# search_field=driver.find_element_by_class_name('mercado-match')

search_field=driver.find_element_by_xpath("//input[@class='search-global-typeahead__input']")
# search_query = input('What profile do you want to scrape? ')
search_field.send_keys('software engineer')
search_field.send_keys(Keys.RETURN)


element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='People']")))
element.click()

#people=driver.find_element_by_xpath("//div[@id='search-reusables__filters-bar']//ul//li[3]//button").click()
people=driver.find_element_by_xpath("//button[text()='People']//parent::li[@class='search-reusables__primary-filter']").click()
print('Searching profiles completed')