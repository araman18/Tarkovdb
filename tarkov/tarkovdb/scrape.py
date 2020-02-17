import sys
from bs4 import BeautifulSoup
import requests

def scrape(item_name):
	arguments = item_name
	start_string = "https://tarkov-market.ru/en/item/"
	l = arguments.split()
	for i in range(0,len(l)):
		start_string += l[i]
		if i != len(l) - 1:
			start_string += "_"

	page = requests.get(start_string)
	soup = BeautifulSoup(page.text, 'html.parser')
	prices = soup.find(class_='price last')
	pretty = prices.prettify()
	lst = pretty.split()
	price = lst[4]
	price = price.replace("₽","")
	price = price.replace(",","")
	num_price = int(price)
	return num_price



