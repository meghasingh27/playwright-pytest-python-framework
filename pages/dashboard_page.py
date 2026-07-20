from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        # Locators

        self.dashboard_heading = page.locator(
            "//h6[text()='Dashboard']"
        )

        self.user_dropdown = page.locator(
            "//span[@class='oxd-userdropdown-tab']"
        )

    # Verification

    def verify_dashboard_loaded(self):

        self.verify_visible(self.dashboard_heading)

        self.verify_text(
            self.dashboard_heading,
            "Dashboard"
        )

    # Click User Menu

    def click_user_dropdown(self):

        self.click(self.user_dropdown)