import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(page, test_name):

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

        file_name = f"{test_name}_{timestamp}.png"

        page.screenshot(
            path=f"screenshots/{file_name}"
        )