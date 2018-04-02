import urllib2
from bs4 import BeautifulSoup
import numpy as np
import csv

rawData = []
data2000 = []
data2001 = []
data2002 = []
data2003 = []
data2004 = []

dates = ['JAN 1ST', 'FEB 1ST', 'MAR 1ST', 'APR 1ST', 'MAY 1ST', 'JUN 1ST', 'JUL 1ST', 'AUG 1ST', 'SEPT 1ST', 'OCT 1ST', 'NOV 1ST', 'DEC 1ST']
years = ['2000', '2001', '2002', '2003', '2004']

# 1. EXTRACT DATA
url = "https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm"

source = urllib2.urlopen(url)

soup = BeautifulSoup(source,'html.parser')

#Locate table with the data
prevTable = soup.find('table', {"summary" :"Henry Hub Natural Gas Spot Price (Dollars per Million Btu)"})

startPoint = prevTable.find('td', {"class":'B4'})

bei = startPoint.find_all_next('td')
	
for each in bei:
	
	item = each.text.encode('ascii','ignore').decode('ascii')

	rawData.append(item)


# 2. CLEAN DATA 
	#2.1 Get yearly data
data2000 = rawData[40:52]
data2001 = rawData[53:65]
data2002 = rawData[66:78]
data2003 = rawData[79:91]
data2004 = rawData[92:104]

corpus = np.array(data2000+data2001+data2002+data2003+data2004)

	#2.2 Assign Dates and write to CSV
with open("monthlyPrices.csv", "a") as dump: #Open the csv file to write the data to
		writer = csv.writer(dump)
		writer.writerow(['YEAR', 'PRICE'])
		j = 0
		k = 0
		m = 0
		p = 0


		while(j<5):
			m = k + 12
			n = 0 
			while(k<m):
				year = dates[n] + ' ' + years[p]
				price = corpus[k]
				writer.writerow([year, price])

				k = k +1
				n = n +1 

			j = j+1
			p = p+1

print("CSV SUCCESSFULLY POPULATED")
			

