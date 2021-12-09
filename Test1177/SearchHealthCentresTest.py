import unittest
import time 
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
        self.driver.get('https://www.1177.se/')

    def test_search_for_health_centres(self):

        actions = ActionChains(self.driver)

        # wait for all elements to load in
        time.sleep(1)
        
        # accept cookies
        accept_cookie_button = self.driver.find_element_by_id("onetrust-accept-btn-handler")
        accept_cookie_button.click()

        # click on find care
        find_care_button = self.driver.find_element_by_class_name('find-care-icon')
        find_care_button.click()
 
        # move to search field and click on it
        self.location_search_field = self.driver.find_element_by_id("location")
        actions.move_to_element(self.location_search_field).perform()

        # clear search field
        self.location_search_field.clear()
        
        # enter search keyword
        self.location_search_field.send_keys("Hela landet")

        # choose alternative and click on it
        select_location_button = self.driver.find_element_by_class_name("findcare-searchfield__autocomplete__item")
        select_location_button.click()

        # search for chosen alternative
        search_care_button = self.driver.find_element_by_class_name('findcare-form__button')
        search_care_button.click()

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
