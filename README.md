# CI Docker autotests
***


## Requirements
* [Python](https://www.python.org/downloads/) (3.12)  
* [Allure](https://allurereport.org/docs/install/) (2.30.0)  
* [Docker](https://www.docker.com/get-started/) (24.0.5)

The Python packages can be installed by running  
```commandline
python3 -m pip install -r requirements.txt
```
***


## Running tests
```commandline
pytest
```
***


### Files and directories:
- `allure-report/index.html` allure report
- `allure-results/` test results directory  
**Note:** These directories will be created after running tests script

* `data/` module with data (links, contact data, urls, browser driver paths)
* `helpers/` helpers modules (cookie helper, driver factory)
* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `create_env_properties_file.py` info file generating script
***
