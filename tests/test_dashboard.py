import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utilities.json_reader import JsonReader


@pytest.mark.regression
def test_dashboard_verification(setup):

    page = setup

    data = JsonReader.read("login.json")

    login = LoginPage(page)

    dashboard = DashboardPage(page)

    login.open(page.environment_url)

    login.login(
        data["username"],
        data["password"]
    )

    dashboard.verify_dashboard_loaded()

    dashboard.click_user_dropdown()