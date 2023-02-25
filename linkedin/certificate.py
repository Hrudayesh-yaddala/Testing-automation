
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
from time import time
# from lxml import etree
# import csv

print('importing finished')
driver=webdriver.Chrome(executable_path='E:\\selenium_webdriver\\chromedriver')
sleep(1)
url = 'https://www.linkedin.com/login'
driver.get(url)
print('Finished initializing a driver')
sleep(1)

username='yaddalahrudayesh@gmail.com'
password='Kingnani@22'
print('Finished importing the login credentials')
sleep(1)

driver.maximize_window()
email_field = driver.find_element_by_id('username')
email_field.send_keys(username)
sleep(1)

password_field = driver.find_element_by_name('session_password')
password_field.send_keys(password)
sleep(1)

signin_field=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
signin_field.click()
sleep(1)

print('finised Login to Linkedin')

# url='https://www.linkedin.com/in/yaddala-hrudayesh-212846226/'
# driver.get('https://www.linkedin.com/in/ishansharma7390/')
# profile_links=['https://www.linkedin.com/in/ishansharma7390/','https://www.linkedin.com/in/yaddala-hrudayesh-212846226/']
with open('data.txt','r') as inputfile:
    links=inputfile.readlines()
    for link in links:
        certificates=[]
        institute=[]
        skilist=[]
        driver.get(link)
        page_source = BeautifulSoup(driver.page_source, "html.parser")
        info_div = page_source.find('div', {'class': 'mt2 relative'})
        name_loc=info_div.find('h1')
        name=name_loc.getText().strip()
        descript_loc = info_div.find("div", {'class': 'text-body-medium break-words'})
        descript=descript_loc.getText().strip()
        locat_loc=info_div.find("span", {'class': 'text-body-small inline t-black--light break-words'})
        locat=locat_loc.get_text().strip()

        driver.get(link+'details/certifications/?profileUrn=urn%3Ali%3Afsd_profile%3AACoAACy8b4oBt7H2NvfVuEiLUDFWMIcaO54UeFw')
        sleep(2)
        cert_source = BeautifulSoup(driver.page_source, "html.parser")
        jobs = cert_source.find_all('div', class_ = 'pvs-list__container')
        for job in jobs[:100]:
            items = job.find_all('span', attrs = {'class' : 'mr1 hoverable-link-text t-bold'})
            institution=job.find_all('span', attrs = {'class' : 't-14 t-normal'})
            for i in range(len(items)):
                # print(items[i].text.strip())
                s=str(items[i].text.strip())
                certificates.append(s[0:(len(s)//2)])
            for i in range(len(institution)):
                s=str(institution[i].text.strip())
                institute.append(s[0:(len(s)//2)])

        driver.get(link+'details/skills/')
        sleep(2)
        skill_source = BeautifulSoup(driver.page_source, "html.parser")
        jobs = skill_source.find_all('div', class_ = 'artdeco-tabs artdeco-tabs--size-t-48 ember-view')
        sleep(1)
        for job in jobs[:100]:
            items = job.find_all('span', attrs = {'class' : 'mr1 hoverable-link-text t-bold'})
            for i in range((len(items)//2)):
                s=str(items[i].text.strip())
                skilist.append(s[0:(len(s)//2)])

    with open('ouputresults.txt','a') as outputfile:
        outputfile.write(f'Name  : {name}\nLocation  : {locat}\nAbout  : {descript}')
        outputfile.write('\n********CERTIFICATIONS********')
        for i in range(len(certificates)):
            outputfile.write(f'\n{certificates[i]}----({institute[i]})')
        outputfile.write('\n********SKILLS****************')
        for i in range(len(skilist)):
            outputfile.write(f'\n{skilist[i]}')
        outputfile.write('\n====================================================================================================================================================================================')



    