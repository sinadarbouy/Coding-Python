import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://www.1177.se/Vastra-Gotaland/")

    def test_search_field(self):
        # check search field exists on Home page
        icon_search = self.driver.find_element(
            By.XPATH,
            '//button[contains(@class, "header-tools__list__item__button header-tools__list__item__button--search-desktop")]',
        )
        icon_search.click()

        input_search = self.driver.find_elements_by_name(
            "q"
        )  # for mobile and big screen
        self.assertTrue(len(input_search) == 2)

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
