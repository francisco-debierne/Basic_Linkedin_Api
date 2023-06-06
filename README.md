# LinkedIn Api.
In this project we will create a python module that can be use to find the LinkedIn URLs and the total of employee of a list of companies provide by CSV file unsing API. 

To do that we will Selenium (https://www.selenium.dev/) and FastApi (https://fastapi.tiangolo.com/).

### Prerequisites

In order to running this correctly it is recomended that you use Python 3.10.5 and have the right Selemium Dirvers in the root folder. If you use Chorme, you can find they right driver in this page https://chromedriver.chromium.org/downloads 

### Input File Format


### Usage

As a first step, install the requirements:
```
pip install -r requirements.txt
```
User and Password

This is how you run the code locally from your terminal:
```
uvicorn main:app --reload
```

### Validation

Once the App is running, you can use the file "input_file.csv" to get some rsult from the aplication. Easist way to do that is using the Interactive API Documentation  http://localhost:8000/docs in your browser. 

Expand the /update_companies_asnyc/ or /update_companies/ route, and you will see a Try it out button. Click that button.

![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/e41bf630-ada4-4d72-84af-c666972f0863)

Select a file then click the Execute button (the blue one)

![image](https://github.com/francisco-debierne/Basic_Linkedin_Api/assets/85453178/690b7b6d-a801-4c9a-9c6b-dffbe751348a)

Denpendens on Route you chosse, you will get diferent mensagem, but in the both process the final result will be storage on uploads folders. 
