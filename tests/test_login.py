import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utilities.json_reader import JsonReader
from utilities.logger import Logger


logger = Logger.get_logger()


@pytest.mark.smoke
def test_valid_login(setup):

    page = setup

    data = JsonReader.read("login.json")

    login = LoginPage(page)

    dashboard = DashboardPage(page)

    logger.info("Opening OrangeHRM")

    login.open(page.environment_url)

    logger.info("Performing Login")

    login.login(
        data["username"],
        data["password"]
    )

    logger.info("Verifying Dashboard")

    dashboard.verify_dashboard_loaded()

    logger.info("Login Test Passed")

'''pytest
↓
conftest.py
↓
Browser Launch
↓
test_login.py
↓
LoginPage
↓
BasePage
↓
Playwright
↓
Browser'''