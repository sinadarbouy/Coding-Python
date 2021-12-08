import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# unittest.TestCase
class HomePageTest:
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

        input_search = self.driver.find_element_by_name("q")
        input_search.clear()
        # enter search keyword and submit
        input_search.send_keys("phones")
        input_search3 = self.driver.find_element(
            By.XPATH,
            '//button[@name="q")]',
        )
        self.assertTrue(len(input_search) == 1)

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()


a = HomePageTest()
a.setUp()
a.test_search_field()

# if __name__ == "__main__":
#     unittest.main(verbosity=2)
