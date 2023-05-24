from selenium import webdriver

import time


from webdriver_manager.chrome import ChromeDriverManager

from UI import UI
from Driver import Driver
from Actions import Actions


class App:
    @staticmethod
    def main():

        test_elements = [
            {"Place": "//input[@name='ss']"},
            {"Date": "//div[@class='b91c144835']"},
            {"Person": "//button[@data-testid='occupancy-config']"},
        ]

        entries = [list(key.keys())[0] for key in test_elements]

        entries_data = UI().fill_enries(entries)

        chrome = Driver(webdriver.Chrome(
            ChromeDriverManager().install()))

        time.sleep(1)

        current_driver = chrome.get_driver()

        Actions(current_driver).test_form(entries_data, test_elements)


if __name__ == "__main__":
    App().main()
