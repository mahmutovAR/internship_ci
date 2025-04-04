#!/bin/bash

pytest --disable-warnings --alluredir=allure-results --clean-alluredir --junitxml=pytest_results
python3 parse_test_results.py
allure generate allure-report --clean --single-file allure-results
zip -r report.zip allure-report
