import unittest
import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class EnglishArticleTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install())
        self.driver.implicitly_wait(1)
        #time.sleep(1)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get('https://www.1177.se/')

    def test_language_box(self):

        actions = ActionChains(self.driver)

        
        cookie = self.driver.find_element_by_id("onetrust-accept-btn-handler")
        button1 = self.driver.find_element_by_css_selector(".c-anchor.c-linklist__link[href=\"/en/other-languages/1177-in-other-languages/\"]:first-child")

        cookie.click()
        time.sleep(2)
        actions.move_to_element(button1).perform()
        time.sleep(2)
        button1.click()
        print("Button1 clicked")
        time.sleep(2)

        
        button2 = self.driver.find_element_by_css_selector("a[href=\"/en/other-languages/other-languages/\"]")

        actions.move_to_element(button2).perform()
        time.sleep(2)
        button2.click()
        print("Button2 clicked")
        time.sleep(2)
        
        




    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)


# document.querySelectorAll(".c-anchor.c-linklist__link)