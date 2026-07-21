import pytest
from playwright.sync_api import sync_playwright

from utilities.config_reader import ConfigReader
from utilities.screenshot import Screenshot


def pytest_addoption(parser):

    parser.addoption(
        "--env",
        action="store",
        default="QA",
        help="Environment : QA/UAT/STAGE"
    )
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser : chromium/firefox/webkit"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run browser in headed mode"
    )


@pytest.fixture(scope="function")
def setup(request):

    playwright = sync_playwright().start()

    browser_name = (
    request.config.getoption("--browser")
    or ConfigReader.get_browser()
    )

    headless = ConfigReader.get_headless()

    if request.config.getoption("--headless"):
        headless = True

    if request.config.getoption("--headed"):
        headless = False

    slow_mo = ConfigReader.get_slow_mo()

    environment = request.config.getoption("--env")

    # Launch Browser

    if browser_name.lower() == "chromium":

        browser = playwright.chromium.launch(
            headless=headless,
            slow_mo=slow_mo
        )

    elif browser_name.lower() == "firefox":

        browser = playwright.firefox.launch(
            headless=headless,
            slow_mo=slow_mo
        )

    elif browser_name.lower() == "webkit":

        browser = playwright.webkit.launch(
            headless=headless,
            slow_mo=slow_mo
        )

    else:

        raise Exception(f"{browser_name} is not supported.")

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )

    page = context.new_page()

    # Store environment URL on page object

    page.environment_url = ConfigReader.get_url(environment)

    yield page

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            Screenshot.capture(
                page,
                request.node.name
            )

    page.close()
    context.close()
    browser.close()
    playwright.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
'''
This file is responsible for

Launch Browser
Create Browser Context
Create Page
Close Browser
'''

'''Browser Context is used because - 
Every test gets

Fresh Cookies
Fresh Session
Fresh Local Storage

Exactly how companies write it.'''