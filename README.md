# LinkedIn Api.
In this project we will create a Python module that can be used to find the LinkedIn URLs and the total of employees of a list of companies provided by CSV file using API. 

To do that we will Selenium (https://www.selenium.dev/) and FastApi (https://fastapi.tiangolo.com/).

### The Playwright Browser. 

For the proposition of this project, we use Selenium as Playwright Browser to run the scraper.

### Prerequisites

To run this correctly, you should use Python 3.10.5 and have the right Selenium Drivers in the root folder. If you use Chrome, you can find the right driver on this page https://chromedriver.chromium.org/downloads

* How to configure the Chrome drivers for Selenium?

  1. Check our Chrome version.
       To do that, open your browser and (1) go to Settings (3 dots right above), (2) then go to the help and (3) click on About Chrome. There will find your Chrome version.     
        
        ![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/09f6acdb-c4a6-4d0b-9404-0020bf1b0876)
  
  2. Download the driver for your Chrome version.
      Go to https://chromedriver.chromium.org/downloads and download the version of the driver close to your actual version.
      
      The first version for the driver is the best option for the case we are describing here. But if you are running an old version of Chrome you should pick the best choice. 
      
      ![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/0c2383c7-5a51-4b9e-8e3b-a933dac1028f)

  3. The final step is to unzip the file and put the chromedriver.exe inside of your root project folder. 
 

### Input File Format

the input file should just have the name of the companies by ",", as in the figure bellow.

![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/07c97485-1dc4-4fa2-8c42-b67875ea99d3)


### Usage

As a first step, install the requirements:
```
pip install -r requirements.txt
```
User and Password

Before starting the process, you must add a USER and PASSWORD to the LinkedIn in the raw 23 and 24. 

![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/bcea039d-9123-4239-8800-3c1d341dc659)

This is how you run the code locally from your terminal:
```
uvicorn main:app --reload
```

### Validation

Once the App is running, you can use the file "input_file.csv" to get some results from the application. The easiest way to do that is using the Interactive API Documentation  http://localhost:8000/docs in your browser. 

Expand the /update_companies_asnyc/ or /update_companies/ route, and you will see a Try it out button. Click that button.

![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/e41bf630-ada4-4d72-84af-c666972f0863)

Select a file then click the Execute button (the blue one)

![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/690b7b6d-a801-4c9a-9c6b-dffbe751348a)

Depending on Route you choose, you will get different messages, but in both process, the final result will be storage on uploads folders.
