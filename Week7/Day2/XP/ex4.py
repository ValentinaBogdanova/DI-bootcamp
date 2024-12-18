# 🌟 Exercise 4 : Scrape and Categorize News Articles from a JavaScript-Enabled News Site
# Task:
# Visit this website.
# Scrape news article titles and their publication dates.
# Categorize articles based on their publication month.
# Instructions:
# Use Selenium to navigate to a specific news section on the website.
# Extract and parse the HTML content that is dynamically loaded via JavaScript.
# Using BeautifulSoup, extract news article titles and publication dates.
# Categorize articles by their publication month (e.g., ‘January’, ‘February’, etc.).
# Print the categorized lists of articles.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
from datetime import datetime
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.bbc.com/innovation/technology")
url = driver.current_url
time.sleep(3)

all_news = []
page_number = 1
try:
      while True: #for pages
        print(f"Parsing page {page_number}...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-da05643e-0.kbaPPZ"))
        )

        #parcing html
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        news_blocks = soup.select("div.sc-93223220-0.sc-da05643e-1.fiJvSm.djXsFQ > div")
        print("Page is parced")

        for news in news_blocks:
            title_tag = news.select_one("h2")
            title = title_tag.text.strip() if title_tag else "No title"

            description_tag = news.select_one("p")
            description = description_tag.text.strip() if description_tag else "No description"

            date_tag = news.select_one("div.sc-ae29827d-1.hAmwyA > div > span")
            date_text = date_tag.text.strip() if date_tag else "No date"

            try:
                pub_date = datetime.strptime(date_text, "%M %d, %Y")
                month = pub_date.strftime("%B")
            except:
                pub_date = None
                month = "Unknown"

            all_news.append({
                "Title": title,
                "Description": description,
                "Publication Date": date_text,
                "Month": month
            })

        try:
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Next Page"]')))
            next_button.click()
            driver.execute_script("arguments[0].click();", next_button)  # Кликаем по кнопке
            print(f"Going to page {page_number + 1}...")
            page_number += 1
            time.sleep(5)
        except Exception:
                print("This is last page. Finishing")
                break

except Exception as e:
    print("Error:", e)

finally:
    df = pd.DataFrame(all_news)
    print("\nCategorized Articles by Month:")
    for month, group in df.groupby("Month"):
        print(f"\n{month}:")
        print(group[["Title", "Publication Date"]])

