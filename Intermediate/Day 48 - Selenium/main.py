from selenium import webdriver

path = r"C:\Users\Mariusz\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://amazon.co.uk")
