# Python API Automation Framework

## Integration Test cases for the Restful Booker

URL - https://restful-booker.herokuapp.com/apidoc/index.html

1. Verify GET, POST, PACTH, DELETE, PUT
2. Response Body, Headers, Status Code.
3. Auth - Basic Auth, Cookie Based Auth.
4. JSON Schema Validation.

## Tech Stack (Python Packages used)
1. Python, Request Module
2. PyTest, PyTest-html
3. Allure Report
4. Faker, CSV, JSON, YAML.
5. Run via Commandline - Jenkins

P.S - DB Connection(in future)


## Install pip packages

``` pip install requests pytest pytest-html faker allure-pytest jsonschema```
```pip install requirements.txt```

## How to run Locally and see the Report?

```pytest tests/* -s -v --alluredir=./reports --html=report.html```









#   P y t h o n A P I - - C u s t o m - - A u t o m a t i o n F r a m e w o r k  
 