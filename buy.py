from numpy import double
import requests
import datetime
import time
from pathlib import Path

now = datetime.datetime.now()
name = "database/buy/" + str(now.year)+"-" + str(now.month) + "-" + str(now.day) + ".txt"

myfile = Path(name)
myfile.touch(exist_ok=True)

def sd(x):
	if x < 10:
		return '0' + str(x)
	return str(x)

mn, mx = 150, 50

with open(name, "r+") as f:
	for line in f:
		val = double(line.split()[2])
		mn = min(mn, val)
		mx = max(mx, val)

	while(1):

		now = datetime.datetime.now()
		request = requests.get("https://www.tinkoff.ru/api/v1/currency_rates/").json()

		for rate in request['payload']['rates']:
			if rate['fromCurrency']['name'] == 'USD' and rate['toCurrency']['name'] == 'RUB' and rate['category'] == 'PrepaidCardsTransfers':
				
				f.write("{}:{}:{} | {}\n".format(sd(now.hour), sd(now.minute), sd(now.second), rate['buy']))

				mx = max(mx, double(rate['buy']))
				mn = min(mn, double(rate['buy']))

				print("{}:{}:{} | mn = {} | mx = {} | cur = {}".format(sd(now.hour), sd(now.minute), sd(now.second), mn, mx, rate['buy']))
				
				time.sleep(30)
			
	f.close()

