from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv
import time
#---Load the urls acquired from scrapy---#
url_list = pd.read_csv('/Users/nicholasmaloof/CodingProjects/WebScrap/groupon/groupon_deals.csv')
#---Going to use Google Chrome---#
driver = webdriver.Chrome()

#---Set up the csv to write the answers in---#
csv_file = open('groupon_reviews.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['author', 'date', 'content', 'url'])

#---Iterate through the list of urls---#
for url in url_list.url:
	try:
		driver.get(url)
		#Close Any Popup That Occurs#
		if(driver.switch_to_alert()):
			close = driver.find_element_by_xpath('//a[@id="nothx"]')
			close.click()
		time.sleep(1)
		try:
			link = driver.find_element_by_xpath('//div[@id="all-tips-link"]')
			driver.execute_script("arguments[0].click();", link)
			time.sleep(2)
		except:
			next
		i = 1
		while True:
			try:
				time.sleep(2)
				print("Scraping Page: " + str(i))
				reviews = driver.find_elements_by_xpath('//div[@class="tip-item classic-tip"]')
				next_bt = driver.find_element_by_link_text('Next')

				for review in reviews[3:]:
					review_dict = {}
					content = review.find_element_by_xpath('.//div[@class="tip-text ugc-ellipsisable-tip ellipsis"]').text
					author = review.find_element_by_xpath('.//div[@class="user-text"]/span[@class="tips-reviewer-name"]').text
					date = review.find_element_by_xpath('.//div[@class="user-text"]/span[@class="tips-reviewed-date"]').text

					review_dict['author'] = author
					review_dict['date'] = date
					review_dict['content'] = content
					review_dict['url'] = url

					writer.writerow(review_dict.values())
				i += 1 
				next_bt.click()
			except:
				break
	except:
		next

csv_file.close()
driver.close()