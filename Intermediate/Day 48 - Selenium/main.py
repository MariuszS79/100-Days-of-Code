from selenium import webdriver
import selenium.webdriver.common.keys
import time

path = r"C:\Users\Mariusz\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

check = time.time() + 5
timeout = time.time() + 60*5

cursor_price = 15
grandma_price = 100
factory_price = 500
mine_price = 2000
shipment_price = 7000
alchemy_lab_price = 50000
portal_price = 1000000
time_machine_price = 123456789


while time.time()<timeout:
    money_web = driver.find_element_by_id("money")
    money = int(money_web.text)
    cookie.click()
    if time.time() > check:
        if money >= time_machine_price:
            tier_8 = driver.find_element_by_id("buyTime machine")
            tier_8.click()
            time_machine_price*=1.1
        elif money >= portal_price:
            tier_7 = driver.find_element_by_id("buyPortal")
            tier_7.click()
            portal_price*=1.1
        elif money >= alchemy_lab_price:
            tier_6 = driver.find_element_by_id("buyAlchemy lab")
            tier_6.click()
            alchemy_lab_price*=1.1
        elif money >= shipment_price:
            tier_5 = driver.find_element_by_id("buyShipment")
            tier_5.click()
            shipment_price*=1.1
        elif money >= mine_price:
            tier_4 = driver.find_element_by_id("buyMine")
            tier_4.click()
            mine_price*=1.1
        elif money >= factory_price:
            tier_3 = driver.find_element_by_id("buyFactory")
            tier_3.click()
            factory_price*=1.1
        elif money >= grandma_price:
            tier_2 = driver.find_element_by_id("buyGrandma")
            tier_2.click()
            grandma_price *= 1.1
        elif money >= cursor_price:
            tier_1 = driver.find_element_by_id("buyCursor")
            tier_1.click()
            cursor_price*=1.1
        check = time.time() + 5

















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
