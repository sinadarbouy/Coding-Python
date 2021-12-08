import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class SearchTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("https://www.ebay.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("gh-ac")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # find_elements_by_class_name
        # //body[contains(@class, 'is-mobile')]

        products = self.driver.find_elements(
            By.XPATH, '//li[contains(@class, "s-item s-item__pl-on-bottom")]'
        )

        # error message in case if test case got failed
        message = "there is no product."

        self.assertGreater(len(products), 0, message)

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
