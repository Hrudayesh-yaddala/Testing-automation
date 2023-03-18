import pandas as pd
import random
from parsel import selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
opts=Options()


driver=webdriver.Chrome(options=opts,executable_path='E:\\selenium_webdriver\\chromedriver')

#function to ensure all key data fields have a value
def validate_field(field):
    #if field is present pass if field
    if field:
        pass
    #if field is not present print text else
    else:
        field="No results"
    return field

#driver.get method() will navigate to a page given by the url address

driver.get('https://www.linkedin.com')

#locate email frorm by_class_name
username=driver.find_element(By.ID,'session_key')

#send_keys() to simulate key strokes
username.send_keys('hrudayesh22@gmail.com')

#sleep for 0.5 seconds
sleep(0.5)

#locate password from by_class_name
password=driver.find_element(By.ID,'session_password')

#send_keys() to simulate key strokes
password.send_keys("Kingnani@22")
sleep(0.5)

#locate submit button by_xpath
sign_in_button=driver.find_element(By.XPATH,'//*[@type="submit"]')

#.click() to mimic button click
sign_in_button.click()
sleep(0.3)


jobdata=[]
lnks=[]
for x in range(0,20,10):
    driver.get(f'https://www.google.com/search?q=site:linkedin.com/in/+AND+%22Python+Developer%22+AND+%22Delhi%22&rlz=1C1HZO_enIN1023&ei=jPaIY-mEGM6cseMpyZaNmAo&start={x}')
    sleep(random.uniform(2.5,4.5))
    linkedin_urls=[my_elem.get_attribute("href") for my_elem in WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='yuRUbf']/a[@href]")))]
    lnks.append(linkedin_urls)

for x in lnks:
    for i in x:

        #get the profile url
        driver.get(i)
        sleep(random.uniform(2.6,4.6))

        #assigning the source code for the web page to variable sel
        sel=selector(text=driver.page_source)

        #xpath to extract the text from the class containing the name
        name=sel.xpath('//*[starts-with@class,"text-heading-xlarge inline t-24 v-align-middle break-words")]/text()').extract_first()

        #if name exists
        if name:
            #.strip() will remove the new line /n and white spaces
            name=name.strip()

        #xpath to extract the text  from the class containing the job title
        job_title=sel.xpath('//*[starts-with@class,"text-body-medium break-words")]/text()').extract_first()

        if job_title:
            job_title=job_title.strip()

        try:
        # xpath to extract the text from the class containing the college
            company=driver.find_element(By.XPATH,'//ul[@class="pv-text-details_right.panel"]').text
        
        except:
            company='None'

        if company:
            company=company.strip()

        # xpath to extract the text from the class containing the location
        location=sel.xpath('//*[starts-with@class,"text-body-small inline t-black--light break-words")]/text()').extract

        if location:
            location=location.strip()

        #validating if the fields exist on the profile
        name=validate_field(name)
        job_title=validate_field(job_title)
        college=validate_field(college)
        company=validate_field(company)
        location=validate_field(location)
        linkedin_url=validate_field(linkedin_url)

        #printing the output
        print('\n')
        print('Name : '+name)
        print('Job Title : '+job_title)
        print('Company : '+company)
        print('Location: '+location)
        print('URL: '+linkedin_url)
        print('\n')

        data={"Name":name,
                "Job Title":job_title,
                "Company": company,
                "Location" :location,
                "URL": linkedin_url}
        jobdata.append(data)

df=pd.DataFrame(jobdata)
df.to_excel('jobdata_linkedin.xlsx')
#terminated the application
driver.quit()
