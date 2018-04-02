import time
import requests
import sys
import pathlib
from selenium import webdriver
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv

# 1. DOWNLOAD THE EXCEL FILE

url = "https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm"


# 1.1 Configure Selenium appropriately
path = 'path/to/driver' #Path to where the Selenium web driver is

download_dir = "path/to/download/directory" # Download to this directory
chrome_options = webdriver.ChromeOptions()
preferences = {"download.default_directory": download_dir ,
               "directory_upgrade": True,
               "safebrowsing.enabled": True }
chrome_options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=path)

driver.get(url);

# 1.2 Download file
time.sleep(5)  # Wait 5 seconds
alll = driver.find_elements_by_class_name('crumb')
alll[1].click()


# 2. EXTRACT SPECIFIC DATA NEEDED

# 2.1 Read from Excel file
df = pd.read_excel('RNGWHHDd.xls', sheetname = 'Data 1')

dates = df['Back to Contents'].values  # Read dates column
dates = dates[2:]  # Actual content start from index 2
prices = df['Data 1: Henry Hub Natural Gas Spot Price (Dollars per Million Btu)'].values  # Read prices column
prices= prices[2:] # Actual content start from index 2

rows = zip(dates, prices)

# 2.2 Write to CSV file
with open("dailyPrices.csv", "a") as dump: #Open the csv file to write the data to
		writer = csv.writer(dump)
		writer.writerow(['Year', 'Price'])

		for row in rows:
			writer.writerow(row)


print("CSV SUCCESSFULLY POPULATED")

