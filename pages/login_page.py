from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        # Locators

        self.username = page.locator("//input[@name='username']")

        self.password = page.locator("//input[@name='password']")

        self.login_button = page.locator("//button[@type='submit']")

    # Actions

    def login(self, username, password):

        self.fill(self.username, username)

        self.fill(self.password, password)

        self.click(self.login_button)