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


@pytest.fixture(scope="function")
def setup(request):

    playwright = sync_playwright().start()

    browser_name = ConfigReader.get_browser()

    headless = ConfigReader.get_headless()

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