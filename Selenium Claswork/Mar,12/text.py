from selenium.webdriver import Chrome, ChromeOptions
o.add_experimental_option("detach", True)
o = ChromeOptions()
driver = Chrome(options=o)

driver.get("https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles")
driver.maximize_window()
driver.title()

driver.back()