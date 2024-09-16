#################	
#				#
#				#
#  TELEGRAM BOT	#
#	 BY VEBY	#
#  TG:@vebytop	#
#				#
#################


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from KeyButton import Keybutton, inKeyButton, inKeyMestopols, Keybutton_2, inKeyRandom, inKeyPassword, inKeyEmail, inKeyPerevod, inKeyTabl, inKeyAnecdot, inlineryletka, inlineryletka_vb, inlineryletka_zd, Keybutton_3, inKeyTabl_1, inKeyTabl_2, InlineCoursVolite, InlineZagatka, InlineS_Treygol, InLinePlayButton, InLinePlay_slovo_Button, Keybutton_4
from commands import DESCRIPTION_COMMANDS, HELP_COMMANDS, START_COMMANDS, INFO_NOMER, INFO_IP, RANDOM_CHIFRA, RANDOM_PASSWORD, RANDOM_EMAIL, PEREVOCHIK_GET, PEREVOCHIK_GET_EN, PEREVOCHIK_GET_RU, CALCULATOR_INFO, TABL_IMNOS_PROV_INFO, tabl_2, tabl_1, GET_POGODA, GET_QRCODE, GET_AUTHOR, S_TREYGOL_GERON, S_TREYGOL_1
from parser_cartinak import main
from random import choice, randint
from Emoji import EMOJI
from Sticker import STICKER
from string import ascii_lowercase, ascii_uppercase, digits
from translate import Translator as tl
from parser_anekdot import get_anekdot
from bs4 import BeautifulSoup as BS
from config import TOKEN_API
from slovar_slov import text_slovar
import time
import requests
import datetime
import qrcode
import os
import gtts
import yaml


with open("config.yaml") as ymlFile:
    config = yaml.load(ymlFile.read(), Loader=yaml.Loader)


bot = Bot(config.get("telegram").get("TOKEN"))
dp = Dispatcher(bot)


data = {}

def get_ip(ip):
	global data
	responce = requests.get(f"http://ip-api.com/json/{ip}").json()

	data = {
		"Страна": responce.get("country"),
		"Код страны": responce.get("countryCode"),
		"Регион": responce.get("region"),
		"Название региона": responce.get("regionName"),
		"Город": responce.get("city"),
		"Почтовый код": responce.get("zip"),
		"Организацыя": responce.get("org"),
		"Ширата": responce.get("lat"),
		"Долгота": responce.get("lon"),
		"Айпи": responce.get("query"),
		"Провайдер": responce.get("isp")
	}


pogoda = {}
wd = ""

def get_pogoda(city, token="2b7393ebef410becc52b6b451aa7c174"):
	global pogoda
	global wd
	req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")

	data = req.json()

	code_to_smile = {
		"Clear": "Ясно \U00002600",
		"Clouds": "Облачно \U00002601",
		"Rain": "Дождь \U00002614",
		"Drizzle": "Дождь \U00002614",
		"Thunderstorm": "Гроза \U000026A1",
		"Snow": "Снег \U0001F328",
		"Mist": "Туман \U0001F32B"
	}


	pod = data["weather"][0]["main"]
	if pod in code_to_smile:
		wd = code_to_smile[pod]
    

	pogoda = {"Город":data["name"],
			"Температура":data["main"]["temp"],
			"Влажность": data["main"]["humidity"],
			"Давление": data["main"]["pressure"],
			"Скорость ветра": data["wind"]["speed"],
			"Погода": wd
			}

dict_data = None

def get_data(phone):
	global dict_data
	responce = requests.get(f"https://phoneradar.ru/phone/{phone}")
	best = BS(responce.text, "lxml")

	data = best.find("tbody").text.split()

	dict_data = {data[0]: data[1:5], data[5]: data[6:8],
				data[8]: data[9]}


async def on_startup(_):
	print("Бот запущен!")

slovo_bot_3 = choice(text_slovar)


@dp.message_handler(commands=["start"])
async def get_start(message: types.message):
	await message.answer(text=START_COMMANDS,
						reply_markup=Keybutton,
						parse_mode="HTML")


@dp.message_handler(commands=["help"])
async def get_help(message: types.message):
	await message.answer(text=HELP_COMMANDS,
						parse_mode="HTML")



@dp.message_handler(commands=["description"])
async def get_deskription(message: types.message):
	await message.answer(text=DESCRIPTION_COMMANDS,
						parse_mode="HTML")




@dp.message_handler(commands=["image"])
async def get_deskription(message: types.message):
	spicok_photo_caption = []
	for photo_img_capt in main(2):
		generat_img_capt = [i.split() for i in photo_img_capt]
		spicok_photo_caption.append(generat_img_capt)

	photo_img_capt = choice(spicok_photo_caption)

	capts = ""
	links = ""

	for capt in photo_img_capt[1]:
		capts += capt
		capts += " "


	for link in photo_img_capt[0]:
		links += link


	await bot.send_photo(chat_id=message.from_user.id,
						photo=links,
						reply_markup=inKeyButton,
						caption=f"{capts}\nНравится данное фото?"
						)



@dp.message_handler(commands=["emoji"])
async def get_emoji(message: types.message):
	await message.answer(text=choice(EMOJI),
						)




@dp.message_handler(commands=["stiker"])
async def get_sticker(message: types.message):
	await bot.send_sticker(chat_id=message.from_user.id,
							sticker=choice(STICKER))



@dp.message_handler(commands=["location"])
async def get_location(message: types.message):
	x = randint(0, 50)
	y = randint(0, 50)
	await bot.send_location(chat_id=message.from_user.id,
							latitude=x,
							longitude=y)

tabl_1_2 = None
tabl_2_2 = None
list_potron = None

legko_chislo = None
sredno_chislo = None
hard_chislo = None


@dp.callback_query_handler()
async def get_callback(callback: types.CallbackQuery):
	global list_potron
	if callback.data == "like":
		await callback.answer(text="Вы поставили лайк!")

		await callback.answer()

	elif callback.data == "dislike":
		await callback.answer(text="Вы паставили дизлайк!")

		await callback.answer()


	elif callback.data == "skip":
		spicok_photo_caption = []
		for photo_img_capt in main(2):
			generat_img_capt = [i.split() for i in photo_img_capt]
			spicok_photo_caption.append(generat_img_capt)

		photo_img_capt = choice(spicok_photo_caption)

		capts = ""
		links = ""

		for capt in photo_img_capt[1]:
			capts += capt
			capts += " "

		for link in photo_img_capt[0]:
			links += link 


		await callback.message.edit_media(types.InputMedia(media=links, # callback.message.edit_media() редоктировать медио файлы types.InputMedia() - для устоновки фотографии media - фотка type - тип
															type="photo",
															caption=f"{capts}\nНравится данное фото?"),
															reply_markup=inKeyButton)
		await callback.answer()

	elif callback.data == "Mesto_polos":
		await bot.send_location(chat_id=callback.from_user.id,
								latitude=data.get("Ширата"),
								longitude=data.get("Долгота"))

		await callback.answer()

	elif callback.data == "sledishye":
		GET_RANDOM_CIFRA_2 = f"""
		<em>
			Случайная цифра 
			в диапозоне {diapozon[0]}-{diapozon[1]} = <b>{randint(diapozon[0], diapozon[1])}</b>
		</em>
		"""
		
		await callback.message.edit_text(text=GET_RANDOM_CIFRA_2,
									parse_mode="HTML",
									reply_markup=inKeyRandom)


		await callback.answer()


	elif callback.data == "password":
		password_list = []
		s = map(str, counts)
		s = ''.join(s)
		s = int(s)
		string_ps = list(ascii_lowercase + ascii_uppercase + digits + "#$")
		password_str = ""

		for count in range(0, s-1):
			pw = randint(0, len(string_ps)-1)
			password_list.append(string_ps[pw])

		for i in password_list:
			password_str += str(i)


		GET_POROL_2 = f"""
		<em>
			Следущий пороль длиной <b>{s}</b> символов
			Успешно  сгенирирован!
			Пароль: <b>{password_str}</b>
		</em>
		"""

		await callback.message.edit_text(text=GET_POROL_2,
									parse_mode="HTML",
									reply_markup=inKeyPassword)

		await callback.answer()

	elif callback.data == "email":
		email_list = []
		s = map(str, counts_2)
		s = ''.join(s)
		s = int(s)
		string_ps = list(ascii_lowercase + ascii_uppercase + digits)
		email = ""

		for count in range(0, s-1):
			email_list.append(string_ps[randint(0, len(string_ps)-1)])

		for i in email_list:
			email += i

		email += "@mail.ru"

		GET_EMAIL_2 = f"""
		<em>
			Следущий рандномный email адрес
			длиной <b>{s}</b> сивлов
			успешно сгенирован
			email: <b>{email}</b>
		</em>
		"""

		await callback.message.edit_text(text=GET_EMAIL_2,
										parse_mode="HTML",
										reply_markup=inKeyEmail)


		await callback.answer()

	elif callback.data == "en_ru":
		await callback.message.answer(text=PEREVOCHIK_GET_EN,
									parse_mode="HTML")
		await callback.answer()


	elif callback.data == "ru_en":
		await callback.message.answer(text=PEREVOCHIK_GET_RU,
									parse_mode="HTML")
		await callback.answer()


	elif callback.data == "sled_premer":
		global tabl_1_2
		global tabl_2_2
		tabl_1_2 = randint(1, 10)
		tabl_2_2 = randint(0, 10)

		TABL_IMNOS_PROV_INFO_2 = f"""
		<em>
			Введите ответ на пример!
			Пример: <b>{tabl_1_2}*{tabl_2_2}</b>
			Ответ: ?
			Что бы написать ответ напишите "/ti ОТВЕТ"
			Обезательно пробел нужен
		</em>
		"""

		await callback.message.edit_text(text=TABL_IMNOS_PROV_INFO_2,
										reply_markup=inKeyTabl,
										parse_mode="HTML")

		await callback.answer()

	elif callback.data == "otvet":
		if tabl_1_2 == None and tabl_2_2 == None:
			TABL_IMNOS_PROV_INFO_2 = f"""
			<em>
				Введите ответ на пример!
				Пример: <b>{tabl_1}*{tabl_2}</b>
				Ответ: {tabl_1 * tabl_2}
				Что бы написать ответ напишите "/ti ОТВЕТ"
				Обезательно пробел нужен
			</em>
			"""
			await callback.message.edit_text(text=TABL_IMNOS_PROV_INFO_2,
											reply_markup=inKeyTabl,
											parse_mode="HTML")

		else:
			TABL_IMNOS_PROV_INFO_2 = f"""
			<em>
				Введите ответ на пример!
				Пример: <b>{tabl_1_2}*{tabl_2_2}</b>
				Ответ: {tabl_1_2 * tabl_2_2}
				Что бы написать ответ напишите "/ti ОТВЕТ"
				Обезательно пробел нужен
			</em>
			"""
			await callback.message.edit_text(text=TABL_IMNOS_PROV_INFO_2,
											reply_markup=inKeyTabl,
											parse_mode="HTML")

		await callback.answer()


	elif callback.data == "anecdot":
		GET_ANECDOT_2 = f"""
		<em>
			Следущий Анекдот:
			<b>{choice(spicok_anekdot)}</b>
		</em>
		"""

		await callback.message.edit_text(text=GET_ANECDOT_2,
										parse_mode="HTML",
										reply_markup=inKeyAnecdot)
		await callback.answer()

	elif callback.data == "1":
		list_potron = ["Потрон", "Мимо", "Мимо", "Мимо", "Мимо", "Мимо"]
		await callback.message.edit_text(text="Выберите действие",
										reply_markup=inlineryletka)
		await callback.answer()

	elif callback.data == "2":
		list_potron = ["Потрон", "Потрон", "Мимо", "Мимо", "Мимо", "Мимо"]
		await callback.message.edit_text(text="Выберите действие",
										reply_markup=inlineryletka)
		await callback.answer()

	elif callback.data == "3":
		list_potron = ["Потрон", "Потрон", "Потрон", "Мимо", "Мимо", "Мимо"]
		await callback.message.edit_text(text="Выберите действие",
										reply_markup=inlineryletka)
		await callback.answer()

	elif callback.data == "4":
		list_potron = ["Потрон", "Потрон", "Потрон", "Потрон", "Мимо", "Мимо"]	
		await callback.message.edit_text(text="Выберите действие",
										reply_markup=inlineryletka)
		await callback.answer()

	elif callback.data == "5":
		list_potron = ["Потрон", "Потрон", "Потрон", "Потрон", "Потрон", "Мимо"]	
		await callback.message.edit_text(text="Выберите действие",
										reply_markup=inlineryletka)
		await callback.answer()

	elif callback.data == "cdatcha":
		await callback.message.edit_text(text="Вы здались!",
											reply_markup=inlineryletka_zd)
		await callback.answer()

	elif callback.data == "Zanogo":
		await callback.message.edit_text(text="Выбирети количества потрон!",
										reply_markup=inlineryletka_vb)
		
		await callback.answer()

	elif callback.data == "vestrel":
		indx = randint(0, 5)
		text_pt = list_potron[indx]
		if text_pt != "Потрон":
			await callback.message.edit_text(text="Вам повезло!",
										reply_markup=inlineryletka_zd)
		else:
			await callback.message.edit_text(text="Вам не повезло!",
										reply_markup=inlineryletka_zd)

	elif callback.data == "dollar":
		req = requests.get("https://www.banki.ru/products/currency/1usd_rub/")
		bs = BS(req.text, "lxml")
		dollar_rub = bs.find("div", class_="currency-table__large-text").text

		await callback.message.edit_text(text=f"Один доллар в рублях = {dollar_rub}",
										reply_markup=InlineCoursVolite)

	elif callback.data == "euro":
		req = requests.get("https://www.banki.ru/products/currency/1eur_rub/")
		bs = BS(req.text, "lxml")
		euro_rub = bs.find("div", class_="currency-table__large-text").text

		await callback.message.edit_text(text=f"Одно евро в рублях = {euro_rub}",
										reply_markup=InlineCoursVolite)

	elif callback.data == "grivni":
		req = requests.get("https://www.banki.ru/products/currency/1uah_rub/")
		bs = BS(req.text, "lxml")
		grivni_rub = bs.find("div", class_="currency-table__large-text").text

		await callback.message.edit_text(text=f"Одна гривна в рублях = {grivni_rub}",
										reply_markup=InlineCoursVolite)
	
	elif callback.data == "zagadka_sled":
		global zagadka_lst
		text_zagatku_2 = f"""
		Загадка: <b>{choice(zagadka_lst)}</b>
		"""
		await callback.message.edit_text(text=text_zagatku_2,
										reply_markup=InlineZagatka,
										parse_mode="HTML")
	
	elif callback.data == "geron":
		await callback.message.edit_text(text=S_TREYGOL_GERON,
										reply_markup=InlineS_Treygol,
										parse_mode="HTML")


	elif callback.data == "vesota_storona":
		await callback.message.edit_text(text=S_TREYGOL_1,
										reply_markup=InlineS_Treygol,
										parse_mode="HTML")

	elif callback.data == "legko":
		global legko_chislo
		text_message = """
		Вы выбрали легкую сложность
		что бы начать угадывать число
		напишите "/yc_l ЧИСЛО"
		"""
		legko_chislo = randint(0, 99)
		
		await callback.message.answer(text=text_message)

	elif callback.data == "srednai":
		global sredno_chislo
		text_message = """
		Вы выбрали легкую сложность
		что бы начать угадывать число
		напишите "/yc_s ЧИСЛО"
		""" 
		sredno_chislo = randint(100, 1000)

		await callback.message.answer(text=text_message)

	elif callback.data == "hard":
		global hard_chislo
		text_message = """
		Вы выбрали легкую сложность
		что бы начать угадывать число
		напишите "/yc_h ЧИСЛО"
		""" 
		hard_chislo = randint(1000, 10000)

		await callback.message.answer(text=text_message)

	elif callback.data == "podckazka_1":
		global slovo_bot_3
		await callback.message.answer(text=f"Длина слова равна {len(slovo_bot_3)}")

	elif callback.data == "podckazka_2":

		await callback.message.answer(text=f"Первая буква слова {slovo_bot_3[0]}")

	elif callback.data == "podckazka_3":
		await callback.message.answer(text=f"Первые три буквы слова {slovo_bot_3[0:3]}")

	elif callback.data == "cdatcha_slovo":
		await callback.message.answer(text=f"Вы сдались загадоное слово бота {slovo_bot_3}")


@dp.message_handler(commands=["info_nomer"])
async def get_info_nomer(message: types.message):
	await message.answer(text=INFO_NOMER,
						parse_mode="HTML")
		

@dp.message_handler(commands=["*"])
async def get_nomer(message: types.message):
	nomer = message.text[3:]
	get_data(nomer)
	GET_MESSAGE = f"""
	<em>	
		Оператор: {dict_data["Оператор:"]}
		Регион: {dict_data["Регион:"]}
		Город: {dict_data["Город:"]}
	</em>
	"""

	await message.answer(text=GET_MESSAGE,
						parse_mode="HTML")

	
@dp.message_handler(commands=["info_ip"])
async def get_info_ip(message: types.message):
	await message.answer(text=INFO_IP,
						parse_mode="HTML")




@dp.message_handler(commands=["ip"])
async def get_ip_info(message: types.message):
	get_ip(message.text[4:])
	GET_IP_INFO = f"""
	<em>
		Страна: {data.get("Страна")}
		Код страны: {data.get("Код страны")}
		Регион: {data.get("Регион")}
		Название региона: {data.get("Название региона")}
		Город: {data.get("Город")}
		Почтовый код: {data.get("Почтовый код")}
		Организацыя: {data.get("Организацыя")}
		Ширата: {data.get("Ширата")}
		Долгота: {data.get("Долгота")}
		Айпи: {data.get("Айпи")}
		Провайдер: {data.get("Провайдер")}
	</em>
	"""
	await message.answer(text=GET_IP_INFO,
						parse_mode="HTML",
						reply_markup=inKeyMestopols)



@dp.message_handler(commands=["Вперед"])
async def get_slet_str(message: types.message):
	await message.answer(text=START_COMMANDS,
						reply_markup=Keybutton_2,
						parse_mode="HTML")


@dp.message_handler(commands=["Назад"])
async def get_slet_str(message: types.message):
	await message.answer(text=START_COMMANDS,
						reply_markup=Keybutton,
						parse_mode="HTML")



@dp.message_handler(commands=["random_chifra"])
async def set_random_chifra(message: types.message):
	await message.answer(text=RANDOM_CHIFRA,
						parse_mode="HTML")

diapozon = []

@dp.message_handler(commands=["ra_1"])
async def get_random_chifra_1(message: types.message):
	global diapozon
	diapozon.append(int(message.text[6:]))


@dp.message_handler(commands=["ra_2"])
async def get_random_chifra_2(message: types.message):
	global diapozon
	diapozon.append(int(message.text[6:]))

	GET_RANDOM_CIFRA = f"""
	<em>
		Случайная цифра 
		в диапозоне {diapozon[0]}-{diapozon[1]} = {randint(diapozon[0], diapozon[1])}
	</em>
	"""

	await message.answer(text=GET_RANDOM_CIFRA,
						parse_mode="HTML",
						reply_markup=inKeyRandom)
	


@dp.message_handler(commands=["random_password"])
async def get_info_ps(message: types.message):
	await message.answer(text=RANDOM_PASSWORD,
						parse_mode="HTML")


counts = []

@dp.message_handler(commands=["pw"])
async def get_pasword(message: types.message):
	global counts
	counts.append(int(message.text[4:]))
	s = map(str, counts)
	s = ''.join(s)
	s = int(s)
	string_ps = list(ascii_lowercase + ascii_uppercase + digits + "#$")
	password_list = []
	for count in range(0, s-1):
		ps = randint(0, len(string_ps)-1)
		password_list.append(string_ps[ps])

	password_str = ""

	for i in password_list:
		password_str += str(i)


	GET_POROL = f"""
	<em>
		Пароль длиной <b>{s}</b> символов
		Успешно сгенирирован!
		Пороль: <b>{password_str}</b>	
	</em>
	"""

	await message.answer(text=GET_POROL,
						parse_mode="HTML",
						reply_markup=inKeyPassword)



@dp.message_handler(commands=["random_email"])
async def get_info_email(message: types.message):
	await message.answer(text=RANDOM_EMAIL,
						parse_mode="HTML")



counts_2 = []

@dp.message_handler(commands=["ei"])
async def get_email(message: types.message):
	global counts_2
	counts_2.append(int(message.text[4:]))
	s = map(str, counts_2)
	s = ''.join(s)
	s = int(s)
	string_ps = list(ascii_lowercase + ascii_uppercase + digits)
	email_list = []

	email = ""

	for count in range(0, s-1):
		email_list.append(string_ps[randint(0, len(string_ps)-1)])


	for i in email_list:
		email += str(i)

	email += "@mail.ru"

	GET_EMAIL = f"""
	<em>
		Рандомный email адрес
		длиной <b>{s}</b> символов
		успешно сгенирирован 
		email: <b>{email}</b>
	</em>
	"""

	await message.answer(text=GET_EMAIL,
						parse_mode="HTML",
						reply_markup=inKeyEmail)


@dp.message_handler(commands=["perevodchik"])
async def get_info_perevod(message: types.message):
	await message.answer(text=PEREVOCHIK_GET,
						parse_mode="HTML",
						reply_markup=inKeyPerevod)


value_ru = []
@dp.message_handler(commands=["en"])
async def get_perevod_en(message: types.message):
	en_slovo = message.text[4:]
	for i in en_slovo:
		if i == "?":
			en_slovo = en_slovo.replace(i, "")

	translator = tl(from_lang="en", to_lang="ru")
	translate_text = translator.translate(en_slovo)
	value_ru.append(translate_text)


	GET_PEREVOD_IN = f"""
	<em>
		Перевод слов <b>{''.join(en_slovo)}</b>
		Выгледит так: <b>{value_ru[-1]}</b>
	</em>
	"""

	await message.answer(text=GET_PEREVOD_IN,
						parse_mode="HTML")


value_en = []
@dp.message_handler(commands=["ru"])
async def get_perevod_ru(message: types.message):
	ru_slovo = message.text[4:]
	translator = tl(from_lang="ru", to_lang="en")
	translate_text = translator.translate(ru_slovo)
	value_en.append(translate_text)


	GET_PEREVOD_IN_2 = f"""
	<em>
		Перевод слов <b>{''.join(ru_slovo)}</b>
		Выгледит так: <b>{value_en[-1]}</b>
	</em>
	"""

	await message.answer(text=GET_PEREVOD_IN_2,
						parse_mode="HTML")



@dp.message_handler(commands=["calculotor"])
async def get_calculator_info(message: types.message):
	await message.answer(text=CALCULATOR_INFO,
						parse_mode="HTML")


@dp.message_handler(commands=["cl"])
async def get_calculator(message: types.message):
	value = message.text[4:]

	CALCULATOR = f"""
	<em>
		Ответ на пример <b>{value}</b>
		равен: <b>{eval(value)}</b>
	</em>
	"""

	await message.answer(text=CALCULATOR,
						parse_mode="HTML")




@dp.message_handler(commands=["tab_imnos_prov"])
async def info_tab_imnos_prov(message: types.message):
	await message.answer(text=TABL_IMNOS_PROV_INFO,
						parse_mode="HTML",
						reply_markup=inKeyTabl
						)


otvet = None
@dp.message_handler(commands=["ti"])
async def get_tab_imnos_prov(message: types.message):
	global otvet
	otvet = (int(message.text[4:]))

	if tabl_1 * tabl_2 == otvet:
		await message.answer(text="Правельно!",
								reply_markup=inKeyTabl_1)

	elif tabl_1_2 != None and tabl_2_2 != None:
		if tabl_1_2 * tabl_2_2 == otvet:
			await message.answer(text="Правельно!",
								reply_markup=inKeyTabl_1)
		else:
			await message.answer(text="Не правельно!",
								reply_markup=inKeyTabl_2)
	else:
		await message.answer(text="Не правельно!",
								reply_markup=inKeyTabl_2)



spicok_anekdot = []
@dp.message_handler(commands=["anecdot"])
async def get_anegdot(message: types.message):
	global spicok_anekdot

	for i in get_anekdot():
		spicok_anekdot.append(i)

	GET_ANECDOT = f"""
	<em>
		Анекдот:
		<b>{choice(spicok_anekdot)}</b>
	</em>
	"""

	await message.answer(text=GET_ANECDOT,
						parse_mode="HTML",
						reply_markup=inKeyAnecdot)



@dp.message_handler(commands=["pogoda"])
async def info_pogoda(message: types.message):
	await message.answer(text=GET_POGODA,
						parse_mode="HTML")



@dp.message_handler(commands=["pg"])
async def g_pogoda(message: types.message):
	try:
		city = message.text[4:]
		get_pogoda(city=city)

		get_info_pogoda = f"""
		<em>
			Город: {pogoda["Город"]}
			Температура: {pogoda["Температура"]}
			Влажность: {pogoda["Влажность"]}
			Давление: {pogoda["Давление"]}
			Скорость ветра: {pogoda["Скорость ветра"]}
			Погода: {wd}
		</em>
		"""
		await message.answer(text=get_info_pogoda,
							parse_mode="HTML")


	except Exception as ex:
		await message.answer(text="Город не найден!")


@dp.message_handler(commands=["ryletka"])
async def cmd_ryletka(message: types.message):
	await message.answer(text="Выбирети количества потрон!",
						reply_markup=inlineryletka_vb)




@dp.message_handler(commands=["Вперед_2"])
async def cmd_vpered_2(message: types.message):
	await message.answer(text=START_COMMANDS,
						parse_mode="HTML",
						reply_markup=Keybutton_3)


@dp.message_handler(commands=["Назад_2"])
async def cmd_vpered_2(message: types.message):
	await message.answer(text=START_COMMANDS,
						parse_mode="HTML",
						reply_markup=Keybutton_2)




@dp.message_handler(commands=["qrcode"])
async def cmd_qrcode(message: types.message):
	await message.answer(text=GET_QRCODE,
						parse_mode="HTML")


url_qrcode = None
@dp.message_handler(commands=["qc"])
async def cmd_qc(message: types.message):
	global url_qrcode
	url_qrcode = message.text[4:]

name_fail = None
@dp.message_handler(commands=["nm"])
async def cmd_nm(message: types.message):
	global name_fail
	name_fail = message.text[4:] + "." + "png"

	img = qrcode.make(url_qrcode)
	img.save(name_fail)
	with open(f"C:\\Users\\veby\\Desktop\\bot_tg\\{name_fail}", "rb") as photo:
		await bot.send_photo(chat_id=message.chat.id,
							photo=photo)

		os.remove(f"C:\\Users\\veby\\Desktop\\bot_tg\\{name_fail}")


@dp.message_handler(commands=["author"])
async def cmd_author(message: types.message):
	await message.answer(text=GET_AUTHOR,
						parse_mode="HTML")


@dp.message_handler(commands=["cours_volite"])
async def cmd_cours(message: types.message):
	await message.answer(text="Выберите валюту!",
						reply_markup=InlineCoursVolite)

zagadka_lst = []

def get_zagatka():
	global zagadka_lst
	req = requests.get("https://2karandasha.ru/zagadki-dlya-detey/s-podvohom")
	bs4 = BS(req.text, "lxml")

	datas = bs4.find_all("a", class_="rpoem-box")

	for data in datas:
		zagadka_lst.append(data.find("div", class_="copy__text").text)



@dp.message_handler(commands=["zagadka"])
async def cmd_zagadka(message: types.message):
	global zagadka_lst
	get_zagatka()
	text_zagatku = f"""
	Загадка: <b>{choice(zagadka_lst)}</b>
	"""
	await message.answer(text=text_zagatku,
						reply_markup=InlineZagatka, 
						parse_mode="HTML")


@dp.message_handler(commands=["S_Treygol"])
async def cmd_treygol(message: types.message):
	await message.answer(text="Что вам известно?",
						reply_markup=InlineS_Treygol)

TREYGOL_A = None
TREYGOL_B = None
TREYGOL_C = None
TREYGOL_P = None
TREYGOL_H = None

@dp.message_handler(commands=["a"])
async def cmd_a(message: types.message):
	global TREYGOL_A
	try:
		TREYGOL_A = float(message.text[2:])
		await message.reply(text="Успешно!")
	except Exception:
		await message.reply(text="Ошибка!, попробуйте снова")


@dp.message_handler(commands=["b"])
async def cmd_b(message: types.message):
	global TREYGOL_B
	try:
		TREYGOL_B = float(message.text[2:])
		await message.reply(text="Успешно!")
	except Exception:
		await message.reply(text="Ошибка!, попробуйте снова")


@dp.message_handler(commands=["c"])
async def cmd_c(message: types.message):
	global TREYGOL_C
	try:
		TREYGOL_C = float(message.text[2:])
		await message.reply(text="Успешно!")
	except Exception:
		await message.reply(text="Ошибка!, попробуйте снова")

@dp.message_handler(commands=["p"])
async def cmd_p(message: types.message):
	global TREYGOL_A
	global TREYGOL_B
	global TREYGOL_C
	global TREYGOL_P
	TREYGOL_P = float(message.text[2:]) / 2
	S_Geron = (TREYGOL_P * (TREYGOL_P-TREYGOL_A) * (TREYGOL_P-TREYGOL_B) * (TREYGOL_P-TREYGOL_C)) ** 0.5
	TEXT = f"Площать треугольника = {float(round(S_Geron, 4))}"

	await message.answer(text=TEXT)

@dp.message_handler(commands=["h"])
async def cmd_h(message: types.message):
	global TREYGOL_H
	global TREYGOL_A
	TREYGOL_H = float(message.text[2:])

	S_Treygol = (TREYGOL_A * TREYGOL_H) * 0.5

	await message.reply(text=f"Площать треугольника = {round(S_Treygol, 4)}")



@dp.message_handler(commands=["text_golos"])
async def cmd_golos(message: types.message):
	text = """
		Отправь текс по инструкции!
		"/gs ТЕКСТ"
	"""

	await message.answer(text=text,
						reply_markup=Keybutton)

# Не работает!
# @dp.message_handler(commands=["gs"])
# async def cmd_gs(message: types.message):
# 	global name_golos	
# 	text = message.text[4:]
# 	golos = gtts.gTTS(text)
# 	golos.save("GOLOS.txt")
# 	time.sleep(5)

# 	await bot.send_document(message.from_user.id, r"C:\Users\veby\Desktop\bot_tg\GOLOS.t",
#                          caption="Привет")
	

@dp.message_handler(commands=["play_chislo"])
async def get_play_chislo(message: types.message):
	get_message = """
	Игра угадай число бота
	выбирете сложность!
	легкая - число от 0-99
	средняя - число от 100-999
	хард - число от 1000-10000
	"""
	await message.reply(text=get_message,
						reply_markup=InLinePlayButton)


@dp.message_handler(commands=["yc_l"])
async def cmd_play_chislo(message: types.message):
	global legko_chislo
	chislo = message.text[6:]

	if int(chislo) == int(legko_chislo):
		await message.reply(text="Вы угадали!")
	else:
		await message.reply(text="Вы не угадали попробуйте снова!")


@dp.message_handler(commands=["yc_s"])
async def cmd_play_chislo_2(message: types.message):
	global sredno_chislo
	chislo = message.text[6:]

	if int(chislo) == int(sredno_chislo):
		await message.reply(text="Вы угадали!")
	else:
		await message.reply(text="Вы не угадали попробуйте снова!")


@dp.message_handler(commands=["yc_h"])
async def cmd_play_chislo_3(message: types.message):
	global hard_chislo
	chislo = message.text[6:]

	if int(chislo) == int(hard_chislo):
		await message.reply(text="Вы угадали!")
	else:
		await message.reply(text="Вы не угадали попробуйте снова!")


@dp.message_handler(commands=["play_slovo"])
async def get_play_slovo(message: types.message):
	help_CMD = """
	Игра угадай слово бота
	вам будет загадоно слова из словаря
	который содержит более 40 тысеч слов
	что бы начать угадывать слова напишите
	"/ps_slovo СЛОВО"
	""" 

	await message.answer(text=help_CMD,
						reply_markup=InLinePlay_slovo_Button)


@dp.message_handler(commands=["ps_slovo"])
async def cmd_play_slovo(message: types.message):
	global slovo_bot_3
	slovo_pl = message.text[10:]

	if slovo_bot == slovo_pl:
		await message.answer(text="Вы угадали слово!")
	else:
		await message.answer(text="Вы не угадали слово!")


@dp.message_handler(commands=["Вперед_3"])
async def cmd_vpered_4(message: types.message):
	await message.answer(text=START_COMMANDS,
						parse_mode="HTML",
						reply_markup=Keybutton_4)


@dp.message_handler(commands=["Назад_3"])
async def cmd_nazad_4(message: types.message):
	await message.answer(text=START_COMMANDS,
						parse_mode="HTML",
						reply_markup=Keybutton_3)



def get_skazka():
	headers = {
  	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
	}

	req = requests.get("https://mishka-knizhka.ru/skazki-narodov-mira/", headers=headers)
	bs4 = BeautifulSoup(req.text, "lxml")

	data = bs4.find_all("article", class_="hentry article-common post-wrap article-common-desktop")

	for i in data:
		href = i.find("a").get("href")
		yield href


@dp.message_handler(commands=["deskrimenant"])
def cmd_deskrimenant(message: types.message): 
	text = """
	Введите a, b, c
	через каманды
	"/a", "/b", "/c"
	"""

	await message.answer(text)

@dp.message_handler(commands=)
def cmd_2_a(message)








if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup,
							skip_updates=True)