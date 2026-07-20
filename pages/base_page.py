from playwright.sync_api import expect
from utilities.logger import Logger
from utilities.screenshot import Screenshot


class BasePage:

    def __init__(self, page):

        self.page = page

        self.logger = Logger.get_logger()

    # ---------------- Navigation ---------------- #

    def open(self, url):

        self.logger.info(f"Opening URL : {url}")

        self.page.goto(url)

    # ---------------- Click ---------------- #

    def click(self, locator):

        self.logger.info("Clicking Element")

        locator.click()

    # ---------------- Fill ---------------- #

    def fill(self, locator, value):

        self.logger.info(f"Entering Value : {value}")

        locator.fill(value)

    # ---------------- Wait ---------------- #

    def wait_for_element(self, locator):

        locator.wait_for()

    # ---------------- Get Text ---------------- #

    def get_text(self, locator):

        return locator.text_content()

    # ---------------- Screenshot ---------------- #

    def take_screenshot(self, file_name):

        Screenshot.capture(
            self.page,
            file_name
        )

    # ---------------- Assertions ---------------- #

    def verify_visible(self, locator):

        expect(locator).to_be_visible()

    def verify_enabled(self, locator):

        expect(locator).to_be_enabled()

    def verify_text(self, locator, expected_text):

        expect(locator).to_have_text(expected_text)

    def verify_url(self, expected_url):

        expect(self.page).to_have_url(expected_url)

    def verify_title(self, expected_title):

        expect(self.page).to_have_title(expected_title)

'''Instead of repeatedly writing, 
locator.click()
locator.fill()

we simply call, 
self.click()
self.fill()'''