import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup


#imports a lot of stuff atm - good luck making sense of it!

URL = "https://www.amazon.co.uk/Intex-Explorer-Two-Person-Kayak-Oars/dp/B00AIQ8LGG/ref=sr_1_2?keywords=kayak&qid=1639423847&sr=8-2"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}


page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())


URL = "https://www.amazon.co.uk/Intex-Explorer-Two-Person-Kayak-Oars/dp/B00AIQ8LGG/ref=sr_1_2?keywords=kayak&qid=1639423847&sr=8-2"

headers = {
  "User-Agent": Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36}


page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

