#!/usr/bin/python
import requests
from hashlib import sha256
from BeautifulSoup import BeautifulSoup
from config import *

def main():
	validation_data = {'orderNumber': sha256(ORDER_NUMBER).hexdigest()}
	validate = requests.post('%s/validate.php' % URL, data=validation_data)

	order_data = {'postcode': sha256(POSTCODE).hexdigest()}
	order = requests.post('%s/order.php' % URL, data=order_data, cookies=validate.cookies)

	soup = BeautifulSoup(order.content)
	headings = ['Parcel number', 'Order status']

	for row in soup.findAll('tr'):
		heading = row.findChild('th').text
		if heading in headings:
			print '\n* %s\n%s\n' % (heading, row.findChild('td').text)

if __name__ == '__main__':
	main()
