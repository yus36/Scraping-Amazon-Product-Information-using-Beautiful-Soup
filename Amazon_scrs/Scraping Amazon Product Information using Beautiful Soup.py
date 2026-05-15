from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Load URLs
with open("amazon.txt", "r") as f:
    data_split = f.read().splitlines()

def soup_maining(urls):
    # Simplified Setup: Selenium 4.6+ handles the driver automatically
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    all_data = []

    for url in urls:
        if not url.strip(): continue
        
        print(f"Opening: {url}")
        driver.get(url)
        time.sleep(4) 

        try:
            # Using get_attribute("textContent") is often more reliable for hidden text
            rating = driver.find_element(By.CSS_SELECTOR, "span.a-icon-alt").get_attribute("textContent")
        except: rating = "N/A"

        try:
            price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
        except: price = "N/A"

        try:
            reviews = driver.find_element(By.ID, "acrCustomerReviewText").text
        except: reviews = "N/A"

        try:
            availability = driver.find_element(By.ID, "availability").text.strip()
        except: availability = "N/A"

        all_data.append({
            "Product_Rating": rating,
            "Price": price,
            "Total_Reviews": reviews,
            "Availability": availability,
        })
        
    driver.quit()
    return all_data

scraped_data = soup_maining(data_split)
df = pd.DataFrame(scraped_data)
df.to_csv('scraped_data.csv', index=False)
print(df)

#Price: The current cost listed on the page.

#	Product Rating: The star rating (e.g., "4.5 out of 5 stars").

#	Total Reviews: How many people have left a review for that product.

#	Availability: Whether the item is currently "In Stock" or "Currently Unavailable".