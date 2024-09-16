#################	
#				#
#				#
#  TELEGRAM BOT	#
#	 BY VEBY	#
#  TG:@vebytop	#
#				#
#################



import requests
from bs4 import BeautifulSoup as BS


def get_anekdot():
	responce = requests.get("https://www.anecdote.tv/no-category/6566-anekdoty-kategorii-b-samye-smeshnye-130-shtuk.html")

	bs4 = BS(responce.text, "lxml")

	datas = bs4.find_all("div", class_="su-note")

	for data in datas:
		anekdot = data.find("div", class_="su-note-inner su-u-clearfix su-u-trim").text
		yield anekdot