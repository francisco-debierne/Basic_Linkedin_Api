# LinkedIn Api.
In this project we will create a python module that can be use to find the LinkedIn URLs and the total of employee of a list of companies provide by CSV file unsing API. 

To do that we will Selenium (https://www.selenium.dev/) and FastApi (https://fastapi.tiangolo.com/).

### Prerequisites

In order to running this correctly it is recomended that you use Python 3.10.5 and have the right Selemium Dirvers in the root folder. If you use Chorme, you can find they right driver in this page https://chromedriver.chromium.org/downloads 

### Usage

As a first step, install the requirements:
```
pip install -r requirements.txt
```
This is how you run the code locally from your terminal:
```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```



Give a CSV file of company names, create a python module that can find
LinkedIn URLs for those companies. The LinkedIn URLs should be stored as a
CSV file. And once that is done, extend the script using Playwright browser
to find the employee count from LinkedIn and store it in the original file
alongside the Company Names.
