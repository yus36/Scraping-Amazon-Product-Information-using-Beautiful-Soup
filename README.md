Amazon Product Scraper
A Python-based web scraper designed to extract product details from Amazon listings, including ratings, prices, review counts, and availability status.

⚠️ Important Note on Bot Detection
Originally, this project was built using the requests and BeautifulSoup libraries. However, standard HTTP requests are currently blocked by Amazon's security measures. When using requests, Amazon identifies the traffic as automated and returns a "Robot Check" page (CAPTCHA) instead of the actual product data. This results in missing data or N/A values. To bypass this, the project has been updated to use Selenium, which automates a real Chrome browser to mimic human behavior.

Features
Automated Browsing: Uses Selenium to load pages exactly as a user would.

Data Extraction: Scrapes:

Product Rating (e.g., 4.5 out of 5 stars)

Price (Whole dollar amount)

Total Number of Reviews

Stock Availability

Batch Processing: Reads multiple URLs from a local amazon.txt file.

Data Export: Saves all results into a structured scraped_data.csv file for analysis.

Prerequisites
Before running the script, ensure you have Python 3.x installed along with the following libraries:

Bash
pip install selenium pandas
Note: You must have Google Chrome installed on your system. Selenium 4.6+ will automatically handle the driver configuration.

How to Use
Prepare your URL list:
Create a file named amazon.txt in the project folder and paste the Amazon product URLs you want to scrape (one per line).

Run the Scraper:

Bash
python "your_script_name.py"
View Results:
Once the script finishes, a file named scraped_data.csv will be created in the same directory.

Configuration
Inside the script, you can adjust the time.sleep(4) value.

Higher values: Safer; gives the page more time to load and prevents Amazon from flagging your IP.

Lower values: Faster; but increases the risk of being blocked.

Disclaimer
This project is for educational purposes only. Please refer to Amazon's robots.txt and Terms of Service regarding web scraping.
