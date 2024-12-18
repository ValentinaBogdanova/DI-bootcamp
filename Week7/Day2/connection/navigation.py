from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.rottentomatoes.com/")
time.sleep(3)

# url = driver.current_url
# print("URL: ", url)

# current_title = driver.title
# print("Title ", current_title)

# assert url == "https://www.rottentomatoes.com/", "ERROR in url"

print(driver.page_source)
time.sleep(3)
# driver.back()
# time.sleep(3)

# driver.forward()
# time.sleep(10)

# driver.refresh()
# time.sleep(3)

