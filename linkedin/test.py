from selenium import webdriver

# Optional argument : if not specified WebDriver will search your system PATH environment variable for locating the chromedriver
driver = webdriver.Chrome(executable_path=r'C:\\path\\to\\chromedriver.exe')
driver.get('https://www.google.co.in')
print("Page Title is : %s" %driver.title)
driver.quit()