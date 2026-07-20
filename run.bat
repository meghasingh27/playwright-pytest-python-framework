@echo off

echo ===========================================
echo      PLAYWRIGHT AUTOMATION FRAMEWORK
echo ===========================================


REM ======================================================
REM                BASIC EXECUTION
REM ======================================================

REM Run Entire Test Suite
pytest

REM Verbose Execution
REM pytest -v

REM Show print() statements
REM pytest -s

REM Verbose + Print Statements
REM pytest -v -s



REM ======================================================
REM                MARKER EXECUTION
REM ======================================================

REM Smoke Suite
REM pytest -m smoke

REM Regression Suite
REM pytest -m regression

REM Exclude Smoke
REM pytest -m "not smoke"

REM Exclude Regression
REM pytest -m "not regression"



REM ======================================================
REM                SPECIFIC TEST EXECUTION
REM ======================================================

REM Run Login Test File
REM pytest tests/test_login.py

REM Run Dashboard Test File
REM pytest tests/test_dashboard.py

REM Run Particular Testcase
REM pytest tests/test_login.py::test_valid_login

REM Run Tests by Keyword
REM pytest -k login

REM Run Dashboard Keyword
REM pytest -k dashboard



REM ======================================================
REM                BROWSER EXECUTION
REM ======================================================

REM Chromium
REM pytest --browser chromium

REM Firefox
REM pytest --browser firefox

REM Webkit
REM pytest --browser webkit



REM ======================================================
REM                ENVIRONMENT EXECUTION
REM ======================================================

REM QA
REM pytest --env QA

REM UAT
REM pytest --env UAT

REM STAGE
REM pytest --env STAGE



REM ======================================================
REM        ENVIRONMENT + BROWSER COMBINATION
REM ======================================================

REM QA Chromium
REM pytest --env QA --browser chromium

REM QA Firefox
REM pytest --env QA --browser firefox

REM UAT Chromium
REM pytest --env UAT --browser chromium

REM Stage Chromium
REM pytest --env STAGE --browser chromium



REM ======================================================
REM                PARALLEL EXECUTION
REM ======================================================

REM 2 Workers
REM pytest -n 2

REM 4 Workers
REM pytest -n 4

REM Automatic Workers
REM pytest -n auto



REM ======================================================
REM            FAILED TEST EXECUTION
REM ======================================================

REM Last Failed Tests
REM pytest --lf

REM Failed Tests First
REM pytest --ff

REM Re-run Failed Tests Twice
REM pytest --reruns 2

REM Stop On First Failure
REM pytest -x



REM ======================================================
REM                HTML REPORT
REM ======================================================

REM HTML Report
REM pytest --html=reports/report.html

REM HTML Report Self Contained
REM pytest --html=reports/report.html --self-contained-html



REM ======================================================
REM                ALLURE REPORT
REM ======================================================

REM Generate Results
REM pytest --alluredir=allure-results

REM Generate Allure Report
REM allure generate allure-results --clean -o allure-report

REM Open Report
REM allure open allure-report

REM Serve Report
REM allure serve allure-results



REM ======================================================
REM                DEBUGGING
REM ======================================================

REM Capture Print Statements
REM pytest -s

REM Detailed Output
REM pytest -vv

REM Disable Warnings
REM pytest --disable-warnings

REM Show Local Variables
REM pytest -l



REM ======================================================
REM                COMBINATIONS
REM ======================================================

REM Smoke + HTML
REM pytest -m smoke --html=reports/report.html

REM Regression + HTML
REM pytest -m regression --html=reports/report.html

REM Smoke + Parallel
REM pytest -m smoke -n 2

REM Regression + Parallel
REM pytest -m regression -n 2

REM QA + Smoke
REM pytest --env QA -m smoke

REM QA + Regression
REM pytest --env QA -m regression

REM UAT + Smoke
REM pytest --env UAT -m smoke

REM Stage + Smoke
REM pytest --env STAGE -m smoke

REM QA + Chromium + Smoke
REM pytest --env QA --browser chromium -m smoke

REM QA + Firefox + Smoke
REM pytest --env QA --browser firefox -m smoke

REM UAT + Chromium + Regression
REM pytest --env UAT --browser chromium -m regression



REM ======================================================
REM                CURRENT COMMAND
REM ======================================================

pytest -m smoke

pause