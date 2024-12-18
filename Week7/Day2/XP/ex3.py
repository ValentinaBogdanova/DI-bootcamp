# 🌟 Exercise 3 : Scrape Dynamic Content from Rotten Tomatoes
# Task:
# Use Selenium to navigate to the Rotten Tomatoes Certified Fresh Movies page.
# Extract the HTML content after it’s fully loaded.
# Use BeautifulSoup to parse and extract the movie titles, scores, and release dates.
# Instructions
# Set up Selenium WebDriver and navigate to the Rotten Tomatoes page.
# Extract the HTML content using driver.page_source.
# Parse the HTML with BeautifulSoup.
# Find and extract the desired movie information.
# Print the extracted data.


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
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.rottentomatoes.com/")
url = driver.current_url
time.sleep(3)


try:
    #path to fresh sertified movies
    movies_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.a--short[data-track='showmore']"))
    )

    actions = ActionChains(driver)
    actions.move_to_element(movies_button).perform()
    

    print('button is found')
    time.sleep(5)

    certified_fresh_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#header-main > rt-header-nav > rt-header-nav-item:nth-child(1) > rt-header-nav-item-dropdown > rt-header-nav-item-dropdown-list:nth-child(1) > ul > li:nth-child(4) > a"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", certified_fresh_button)
    driver.execute_script("arguments[0].click();", certified_fresh_button)

    print("Clicked")
    time.sleep(5)

    #parcing HTML
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    movies_data = []
    movie_cards = soup.select("tile-dynamic")

    for card in movie_cards:
        title_tag = card.select_one("a > span.p--small")
        title = title_tag.text.strip() if title_tag else "No title"

        score_tag = card.select_one("a > score-pairs-deprecated > rt-text:nth-child(2)")
        score = score_tag.text.strip() if score_tag else "No score"

        release_date_tag = card.select_one("a > span.smaller")
        release_date = release_date_tag.text.strip() if release_date_tag else "No release date"

        movies_data.append({
            "Title": title,
            "Score": score,
            "Release Date": release_date
        })

        df = pd.DataFrame(movies_data)
        df_cleaned = df.loc[(df["Title"] != "No title") & (df["Score"] != "No score") & (df["Release Date"] != "No release date")]

        print(df_cleaned)



except Exception as e:
    print("Issue:", e)

finally:
    driver.quit()

