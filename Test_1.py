from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#Question-1
# driver.get("https://amazon.in")
# sleep(2)
# driver.maximize_window()
#
# a=driver.find_elements("class name","nav-a")
# sleep(2)
# for i in a:
#     print(i.text)
#
# driver.quit()


#Question-2
# driver.get("https://www.imdb.com/chart/top/")
# sleep(3)
# driver.maximize_window()
#
# a=driver.find_elements("class name","ipc-title__text")
# for i in range(11):
#     print(a[i].text)
#
# driver.quit()

#Question-3
# driver.get("https://amazon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# a=driver.find_elements("xpath","//img")
# print(len(a))
# driver.quit()

#Question-5
# driver.get("https://amazon.in")
# sleep(4)
# driver.maximize_window()
# ab=driver.find_elements("xpath","//a")
# for i in ab:
#     print(i.get_attribute("href"))

# #Question-6
# driver.get("https://amazon.in")
# sleep(2)
# driver.maximize_window()
# driver.find_element("id","twotabsearchtextbox").send_keys("Samsung")
# sleep(2)
# a=driver.find_elements("class name","s-suggestion-container")
# for i in a:
#     print(i.text)

#Question-7

# driver.get("https://amazon.in/")
# driver.maximize_window()
#
# sleep(2)
# a=driver.find_element("id","nav-link-accountList")
# o = ActionChains(driver)
# o.move_to_element(a).perform()
# sleep(2)
# driver.find_element("link text","Your Wish List").click()

#Question 8

# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
# driver.maximize_window()
# a=driver.find_element("xpath","//iframe[@id='iframeResult']")
# driver.switch_to.frame(a)
#
# b = driver.find_element("xpath","//iframe[@src = 'demo_iframe.htm']")
# driver.switch_to.frame(b)
# c = driver.find_element("xpath","//h1")
# print(c.text)


#Question-9
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# a = driver.find_element("id", "twotabsearchtextbox")
# a.send_keys("Laptop")
# a.send_keys(Keys.ENTER)
# sleep(2)
# a = driver.find_elements("xpath", "//h2//span")
# for i in a:
#     print(i.text)