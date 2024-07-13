import os

    

import urllib.request
import json
import random  # Importing the random module
import threading
import requests

banner = """

─╔╗────────────────╔╗
╔╝╚╗──────────────╔╝╚╗
╚╗╔╬══╦═╦═╦══╦═╦╦═╩╗╔╝
─║║║║═╣╔╣╔╣╔╗║╔╬╣══╣║
─║╚╣║═╣║║║║╚╝║║║╠══║╚╗
─╚═╩══╩╝╚╝╚══╩╝╚╩══╩═╝
=========================
Dev : @ikea_basic & @archangellov
Channel : @forever_termux
=========================
1. сносер аккаунта
2. сносер тгк
3. сносер сессий
4. бомбер тг
5. разбан номера
6. информация
7. выход 


"""

print(banner)

choice = input("Введите номер желаемой функции -> ")
if choice == "1":
    os.system("clear")
    os.system("python report.py")

if choice == "2":
    os.system("clear")
    os.system("python snostgk.py")
    
if choice == "3":
    os.system("clear")
    os.system("python sessions.py")

if choice == "4":
    os.system("clear")
    os.system("python bomber.py")

if choice == "5":
    os.system("clear")
    os.system("python unbun.py")

if choice == "6":
   print("наш канал @forever_termux. | люблю хомку.")
   
if choice == "7":
      print("удачи вам!")

if choice == "1488":
    print("ПАСХАЛКО ПАСХАЛКО, ВРУБАЕМ ВЕНТИЛЯТОРЫ")
   
if choice == "1227":
    print("тгк мяучело ахаха")