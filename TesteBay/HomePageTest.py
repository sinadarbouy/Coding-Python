import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get('https://www.ebay.com/')

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(
            len(self.driver.find_elements_by_css_selector('#gh-ac')) == 1)

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = self.driver.find_element_by_class_name(
            'gh-cart-icon'
        )

        # just hoever
        actions = ActionChains(self.driver)
        actions.move_to_element(shopping_cart_icon).perform()

        shopping_cart_status = \
            self.driver.find_element(
                By.XPATH, '//h2[@class="gh-minicart-header__title "]'
            ).text
        self.assertEqual("Your cart is empty",
                         shopping_cart_status)

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
