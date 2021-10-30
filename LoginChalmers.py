from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


cid = input('Enter CID \n')
password = input('Enter password \n')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://chalmers.instructure.com')
print('Opened login')

sleep(1)


CID_box = driver.find_element_by_id('userNameInput')
CID_box.send_keys(cid)
print('CID Entered')
sleep(1)


Pass_box = driver.find_element_by_id('passwordInput')
Pass_box.send_keys(password)
print('password Entered')
sleep(1)


login_button = driver.find_element_by_id('submitButton')
login_button.click()


CID_box = driver.find_element_by_id('userNameInput')


print("Done")
input('Press anything to quit \n')
driver.quit()
print("Finished")
