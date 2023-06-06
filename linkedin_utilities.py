
import pandas as pd
from io import BytesIO
import datetime
import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
import warnings
warnings.simplefilter("ignore")

# Configuring the logs
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Constants
XPATH_TOTAL_EMPLOYEES = ["/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[4]", "/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[4]"]
XPATH_ABOUT_SECTION_OPTIONS = ["/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/nav/ul/li[2]/a","/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/nav/ul/li[2]/a"]
LOGIN_URL = 'https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
USER = 'francisco.debierne@gmail.com'
PASSWORD = 'Fra942516'

def login():
    "Create a new Chrome session and login in Linkedin"
    
    # Create a new Chrome session
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    url = driver.command_executor._url 
    session_id = driver.session_id 
    try:
        driver.get(LOGIN_URL)
    except:
        logging.error("Error in the login")
    # Login in Linkedin
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(USER)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys(PASSWORD)
    driver.implicitly_wait(15)
    #Clicando em pular confirmação de seguranção.
    driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
    
    logging.info("Logged in Linkedin")
    return driver


def get_company_link (driver: webdriver.Chrome,company_name: list) -> str:
    " Get the link of the company"
    
    # Acess the search page
    try:
        link_search = f"https://www.linkedin.com/search/results/companies/?keywords={company_name}&origin=SWITCH_SEARCH_VERTICAL"
        driver.get(link_search)
    except:
        logging.error("Error in the search page")
        
    # Clicking in the first result as the company linkedin page
    try:
        driver.find_elements_by_class_name("reusable-search__result-container")[0].click()
        time.sleep(5)
    except:
        logging.error(f"Error to find the company page for {company_name} ")
    
    # Getting the link of the company
    company_link = driver.current_url
    
    logging.info(f"Get the link of the company: {company_name}")
    return company_link

def get_total_employees(driver:webdriver.Chrome):
    " Get the total of employees"
    
    # Geting the right xpath for the about section
    
    for i in range (len(XPATH_ABOUT_SECTION_OPTIONS)):
        try:
            driver.find_element_by_xpath(XPATH_ABOUT_SECTION_OPTIONS[i])
            xpath_about_section = XPATH_ABOUT_SECTION_OPTIONS[i]
            xpath_for_total_employees = XPATH_TOTAL_EMPLOYEES[i]
            break
        except:
            pass
        
    #Clicking in about section
    try:
        driver.find_element_by_xpath(xpath_about_section).click()
        time.sleep(1)
    except:
        logging.error("Error to click in about section")
        
    #Getting the total of employees 
    total_of_employees =  driver.find_element_by_xpath(xpath_for_total_employees).text.split(" ")[0]
    
    logging.info(f"Get the total of employees: {total_of_employees}")
    return total_of_employees

def run (companies_list, date:str):
    "Get the companies informatios for all the companies in the list and save in a csv file"
    
    # Login in Linkedin
    driver = login()
    list_of_info = []
    
    # Get the companies informations
    for company in companies_list:
        company_link = get_company_link (driver,company)
        total_of_employees = get_total_employees(driver)
        new_company_infos = [company, company_link, total_of_employees]
        list_of_info.append(new_company_infos)

    # Close the driver
    driver.close()
    
    # Save the data in a csv file
    df = pd.DataFrame(list_of_info, columns=["Company Name", "Link", "Total of Employees"])
    df.to_csv(f"uploads/companies_info_{date}.csv", index=False)
    
    logging.info(f"Save the data in a csv file: companies_info_{date}.csv")
    return df