#################	
#				#
#				#
#  TELEGRAM BOT	#
#	 BY VEBY	#
#  TG:@vebytop	#
#				#
#################


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



Keybutton = ReplyKeyboardMarkup(resize_keyboard=True)

button_1 = KeyboardButton(text="/help")
button_2 = KeyboardButton(text="/description")
button_3 = KeyboardButton(text="/start")
button_4 = KeyboardButton(text="/image")
button_5 = KeyboardButton(text="/emoji")
button_6 = KeyboardButton(text="/stiker")
button_7 = KeyboardButton(text="/location")
button_8 = KeyboardButton(text="/info_nomer")
button_9 = KeyboardButton(text="/info_ip")
button_10 = KeyboardButton(text="/Вперед")

Keybutton.add(button_3, button_1).add(button_2, button_4).add(button_5, button_6).add(button_7, button_8).add(button_9, button_10)



inKeyButton = InlineKeyboardMarkup(row_width=2)


inButton_1 = InlineKeyboardButton(text="Следущая",
								callback_data="skip")

inButton_2 = InlineKeyboardButton(text="like",
								callback_data="like")

inButton_3 = InlineKeyboardButton(text="dislike",
								callback_data="dislike")


inKeyButton.add(inButton_1, inButton_2).add(inButton_3)


inKeyMestopols = InlineKeyboardMarkup(row_width=2)

inKeyButton_mesto = InlineKeyboardButton(text="Покозать местоположение на карте!",
									callback_data="Mesto_polos")

inKeyMestopols.add(inKeyButton_mesto)

Keybutton_2 = ReplyKeyboardMarkup(resize_keyboard=True)

button_1_2 = KeyboardButton(text="/Назад") 
button_2_2 = KeyboardButton(text="/random_chifra")
button_3_2 = KeyboardButton(text="/random_password")
button_4_2 = KeyboardButton(text="/random_email")
button_5_2 = KeyboardButton(text="/perevodchik")
button_6_2 = KeyboardButton(text="/calculotor")
button_7_2 = KeyboardButton(text="/tab_imnos_prov")
button_8_2 = KeyboardButton(text="/anecdot")
button_9_2 = KeyboardButton(text="/pogoda")
button_10_2 = KeyboardButton(text="/Вперед_2")
Keybutton_2.add(button_1_2, button_2_2).add(button_3_2, button_4_2).add(button_5_2, button_6_2).add(button_7_2, button_8_2).add(button_9_2, button_10_2)

Keybutton_3 = ReplyKeyboardMarkup(resize_keyboard=True)
button_1_3 = KeyboardButton(text="/Назад_2")
button_2_3 = KeyboardButton(text="/ryletka")
button_3_3 = KeyboardButton(text="/qrcode")
button_4_3 = KeyboardButton(text="/cours_volite")
button_5_3 = KeyboardButton(text="/zagadka")
button_6_3 = KeyboardButton(text="/S_Treygol")
button_7_3 = KeyboardButton(text="/text_golos")
button_8_3 = KeyboardButton(text="/play_chislo")
button_9_3 = KeyboardButton(text="/play_slovo")
button_10_3 = KeyboardButton(text="/Вперед_3")
Keybutton_3.add(button_1_3, button_2_3).add(button_3_3, button_4_3).add(button_5_3, button_6_3).add(button_7_3, button_8_3).add(button_9_3, button_10_3)

Keybutton_4 = ReplyKeyboardMarkup(resize_keyboard=True)

button_1_4 = KeyboardButton(text="/Назад_3")
button_2_4 = KeyboardButton(text="/play_skazka")
button_3_4 = KeyboardButton(text="/deskrimenant")
Keybutton_4.add(button_1_4, button_2_4).add(button_3_4)



inKeyRandom = InlineKeyboardMarkup(row_width=2)

inKeyButton_rd = InlineKeyboardButton(text="Следущий",
									callback_data="sledishye")

inKeyRandom.add(inKeyButton_rd)

inKeyPassword = InlineKeyboardMarkup(row_width=2)
inKeyButton_pw = InlineKeyboardButton(text="Следущий",
									callback_data="password")

inKeyPassword.add(inKeyButton_pw)

inKeyEmail = InlineKeyboardMarkup(row_width=2)
inKeyButton_em = InlineKeyboardButton(text="Следущий",
									callback_data="email")

inKeyEmail.add(inKeyButton_em)

inKeyPerevod = InlineKeyboardMarkup(row_width=2)
inKeyButton_pv = InlineKeyboardButton(text="Англиский",
										callback_data="en_ru")

inKeyButton_pv_2 = InlineKeyboardButton(text="➔",
										callback_data="en_ru")

inKeyButton_pv_3 = InlineKeyboardButton(text="Русский",
										callback_data="en_ru")


inKeyButton_pv_4 = InlineKeyboardButton(text="Русский",
										callback_data="ru_en")

inKeyButton_pv_5 = InlineKeyboardButton(text="➔",
										callback_data="ru_en")

inKeyButton_pv_6 = InlineKeyboardButton(text="Англиский",
										callback_data="ru_en")

inKeyPerevod.add(inKeyButton_pv, inKeyButton_pv_2, inKeyButton_pv_3).add(inKeyButton_pv_4, inKeyButton_pv_5, inKeyButton_pv_6)

inKeyTabl = InlineKeyboardMarkup(row_width=2)

inKeyTabl_button_1 = InlineKeyboardButton(text="Следущий",
										callback_data="sled_premer") 

inKeyTabl_button_2 = InlineKeyboardButton(text="Покозать ответ!",
										callback_data="otvet")

inKeyTabl.add(inKeyTabl_button_1).add(inKeyTabl_button_2)


inKeyTabl_1 = InlineKeyboardMarkup(row_width=2)

inKeyTabl_button_1_2 = InlineKeyboardButton(text="Следущий",
										callback_data="sled_premer") 

inKeyTabl_1.add(inKeyTabl_button_1_2)

inKeyTabl_2 = InlineKeyboardMarkup(row_width=2)

inKeyTabl_button_2_2 = InlineKeyboardButton(text="Покозать ответ!",
										callback_data="otvet")

inKeyTabl_2.add(inKeyTabl_button_2_2)



inKeyAnecdot = InlineKeyboardMarkup(row_width=2)

inKetButton_anecdot = InlineKeyboardButton(text="Следущий",
										callback_data="anecdot")


inKeyAnecdot.add(inKetButton_anecdot)

inlineryletka_vb = InlineKeyboardMarkup(row_width=2)

inlineryletka_vb_1 = InlineKeyboardButton(text="1 потрон",
										callback_data="1")
inlineryletka_vb_2 = InlineKeyboardButton(text="2 потрона",
										callback_data="2") 
inlineryletka_vb_3 = InlineKeyboardButton(text="3 потрона",
										callback_data="3")
inlineryletka_vb_4 = InlineKeyboardButton(text="4 потрона",
										callback_data="4")
inlineryletka_vb_5 = InlineKeyboardButton(text="5 потрон",
										callback_data="5")

inlineryletka_vb.add(inlineryletka_vb_1, inlineryletka_vb_2).add(inlineryletka_vb_3, inlineryletka_vb_4).add(inlineryletka_vb_5)

inlineryletka = InlineKeyboardMarkup(row_width=2)
inlineryletka_bt = InlineKeyboardButton(text="Выстрел🔫",
										callback_data="vestrel")

inlineryletka_bt_2 = InlineKeyboardButton(text="Сдатся☠︎",
										callback_data="cdatcha")
inlineryletka.add(inlineryletka_bt, inlineryletka_bt_2)

inlineryletka_zd = InlineKeyboardMarkup(row_width=2)
inlineryletka_zd_bt = InlineKeyboardButton(text="Начать заного",
										callback_data="Zanogo")
inlineryletka_zd.add(inlineryletka_zd_bt)

InlineCoursVolite = InlineKeyboardMarkup(row_width=2)
InlineCoursVolite_but = InlineKeyboardButton(text="Доллар",
											callback_data="dollar")

InlineCoursVolite_but_2 = InlineKeyboardButton(text="Евро",
											callback_data="euro")

InlineCoursVolite_but_3 = InlineKeyboardButton(text="Гривны",
											callback_data="grivni")

InlineCoursVolite.add(InlineCoursVolite_but, InlineCoursVolite_but_2).add(InlineCoursVolite_but_3)

InlineZagatka = InlineKeyboardMarkup(row_width=2)
InlineZagatka_bt = InlineKeyboardButton(text="Следущая!",
										callback_data="zagadka_sled")
InlineZagatka.add(InlineZagatka_bt)

InlineS_Treygol = InlineKeyboardMarkup(row_width=2)
InlineS_Treygol_bt = InlineKeyboardButton(text="3 стороны и периметр",
										callback_data="geron")

InlineS_Treygol_bt_2 = InlineKeyboardButton(text="1 сторона и высота",
											callback_data="vesota_storona")

InlineS_Treygol.add(InlineS_Treygol_bt, InlineS_Treygol_bt_2)

InLinePlayButton = InlineKeyboardMarkup(row_width=2)
InLinePlayButton_1 = InlineKeyboardButton(text="Сложность - легкая",
										callback_data="legko")

InLinePlayButton_2 = InlineKeyboardButton(text="Сложность - средняя",
										callback_data="srednai")

InLinePlayButton_3 = InlineKeyboardButton(text="Сложность - хард",
										callback_data="hard")

InLinePlayButton.add(InLinePlayButton_1).add(InLinePlayButton_2).add(InLinePlayButton_3)


InLinePlay_slovo_Button = InlineKeyboardMarkup(row_width=2)

InLinePlay_slovo_Button_1 = InlineKeyboardButton(text="Подсказка №1",
												callback_data="podckazka_1")

InLinePlay_slovo_Button_2 = InlineKeyboardButton(text="Подсказка №2",
												callback_data="podckazka_2")

InLinePlay_slovo_Button_3 = InlineKeyboardButton(text="Подсказка №3",
												callback_data="podckazka_3")

InLinePlay_slovo_Button_4 = InlineKeyboardButton(text="Сдатся",
												callback_data="cdatcha_slovo")

InLinePlay_slovo_Button.add(InLinePlay_slovo_Button_1, InLinePlay_slovo_Button_2).add(InLinePlay_slovo_Button_3, InLinePlay_slovo_Button_4)
