import os
import pandas as pd
from io import BytesIO
import datetime
import logging
import warnings

warnings.simplefilter("ignore")

from selenium import webdriver
from selenium.webdriver import ActionChains
from fastapi import FastAPI, File, UploadFile, BackgroundTasks

from linkedin_utilities import run

# Configuring the logs
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG ,format='%(name)s - %(levelname)s - %(message)s')

# Constants
XPATH_TOTAL_EMPLOYEES = ["/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[4]", "/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[4]"]
XPATH_ABOUT_SECTION_OPTIONS = ["/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/nav/ul/li[2]/a","/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/nav/ul/li[2]/a"]
LOGIN_URL = 'https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
USER = '########@######'
PASSWORD = '###########'


app = FastAPI()

@app.post("/update_companies_asnyc/")
async def create_upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    ''' This function will run the update in the background. 
        So the user can continue using the app and make multiple requests at the same time '''
    # Getting the date the request was made
    date = datetime.datetime.now().strftime("%Y.%m.%d %H.%M.%S")
    
    # Reading the input file
    try:
        contents = file.file.read()
        data = BytesIO(contents)
        df = pd.read_csv(data,header=None)
        data.close()
        file.file.close()
    except:
        return {"message": "Error reading the file. Please check the format and try again."}
    
    # Running the update in the background
    background_tasks.add_task(run,df.iloc[0].to_list(), date)
    
    return {"message": f"The update will be done in the background. The result will be stored in the file companies_info_{date}.csv on Uploads"}

@app.post("/update_companies/")
async def create_upload_file(file: UploadFile):
    ''' This function will run the update. Returns the result in a csv file and send it to the user on the response.
        The user will have to wait until the update is done to continue using the app. 
        Multiple requests at the same time its possible '''
    
    # Getting the date the request was made
    date = datetime.datetime.now().strftime("%Y.%m.%d %H.%M.%S")
    
    # Reading the input file
    try:
        contents = file.file.read()
        data = BytesIO(contents)
        df = pd.read_csv(data,header=None)
        data.close()
        file.file.close()
    except:
        return {"message": "Error reading the file. Please check the format and try again."}
    
    # Running the update
    output = run(df.iloc[0].to_list(), date)
    
    return output
