#################	
#				#
#				#
#  TELEGRAM BOT	#
#	 BY VEBY	#
#  TG:@vebytop	#
#				#
#################


from bs4 import BeautifulSoup
import requests
from random import choice

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36'
}


def main(count: int):
	global headers
	for coun in range(1, count):
		req = requests.get(f"https://ru.freepik.com/photos/nature/{coun}", headers=headers)
		soup = BeautifulSoup(req.text, "lxml")

		datas = soup.find_all("figure", class_="showcase__item js-detail-data caption showcase__item--with-tags showcase__item--buttons")

		for data in datas:
			url = data.find("img").get("data-src")
			caption = data.find("img").get("alt")
			
			for i in caption.split():
				if i.lower() == "бесплатное" or i.lower() == "фото":
					caption = caption.replace(i, "")

			yield url, caption