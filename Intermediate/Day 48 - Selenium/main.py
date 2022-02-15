from selenium import webdriver
import selenium.webdriver.common.keys
from threading import Timer

path = r"C:\Users\Mariusz\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

def click():
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    Timer(0.00001, click).start()

click()





# name = driver.find_element_by_class_name("top")
# name.send_keys("Mariusz")
#
#
# surname = driver.find_element_by_class_name("middle")
# surname.send_keys("So")
#
# email = driver.find_element_by_class_name("bottom")
# email.send_keys("m@o2.eu")
#
# signup = driver.find_element_by_class_name("btn")
# signup.click()



#driver.quit()
