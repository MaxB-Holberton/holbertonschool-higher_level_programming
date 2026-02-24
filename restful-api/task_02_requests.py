#!/usr/bin/python3
"""
	Module to show basic api requests and saving them in csv
"""
import requests
import csv

def fetch_and_print_posts():
	"""
		Get the data and print the titles
	"""
	res = requests.get('https://jsonplaceholder.typicode.com/posts')
	print(f"Status Code: {res.status_code}")

	if res.status_code == 200:
		for item in res.json():
			print(item["title"])

def fetch_and_save_posts():
	"""
		Get the data and save to csv
	"""
	res = requests.get('https://jsonplaceholder.typicode.com/posts')

	if res.status_code == 200:
		data = []
		for item in res.json():
			new_item = {
					'id': item.get('id'),
					'title': item.get('title'),
					'body': item.get('body')
				}
			data.append(new_item)

		with open('posts.csv', mode='w') as csv_f:
			newfile = csv.DictWriter(csv_f, fieldnames=['id','title', 'body'])
			newfile.writeheader()
			newfile.writerows(data)
