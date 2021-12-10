import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SearchMedInfoTest(unittest.TestCase): 

    @classmethod
    def setUp(self): 
        # create a new Chrome session
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('https://www.1177.se/')
    
    def test_search_medical_info(self): 

        # accept cookies
        accept_cookie_button = self.driver.find_element_by_id("onetrust-accept-btn-handler")
        self.driver.execute_script("arguments[0].click();", accept_cookie_button)
        #accept_cookie_button.click()

        # find search button and click on it
        search_button = self.driver.find_element_by_class_name("search-icon")
        self.driver.execute_script("arguments[0].click();", search_button)
        #search_button.click()

        # find search field and clear it 
        search_field = self.driver.find_element_by_id("globalsearch")
        search_field.clear()
         
        # enter search keyword 
        search_field.send_keys("covid")
        search_field.submit()

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
