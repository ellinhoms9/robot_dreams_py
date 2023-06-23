import requests
import random

Google = "https://google.com"
Facebook = "https://facebook.com"
Twitter = "https://twitter.com"
Amazon = "https://amazon.com"
Apple = "https://apple.com"

list_of_sites = [Google, Facebook, Twitter, Amazon, Apple]

r_choise = random.choice(list_of_sites)
res = requests.get(r_choise)
print(f"Name of site: {r_choise}")
print(f"Status code: {res.status_code}")
print(f"Length HTML: {len(res.text)})")
