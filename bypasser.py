import requests
import json


def Bypasser(url):
	url = f"https://api.jiroawesome.tech/tools/bypass?link={url}"
	req = requests.get(url)
	hh = json.loads(req.text)
	yy = hh["result"]
	print(f"Result: {yy}")


try:
	h = input("Enter your shortened link: ")
	Bypasser(h)
except:
	print("Unsupported link. Please visit https://api.jiroawesome.tech/supported for more information.")
	input()
