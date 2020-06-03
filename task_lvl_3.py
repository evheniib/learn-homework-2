"""
Задачи
1. Описать принятие и валидацию введенной строки пользователем
2. Описать проверку города на наличие в cvs
3. Сохранять валидные города в список
4. Сделать функцию для начала игры с обьявлением игроков и очереди (рандом)
5. Сделать мастер функцию, которая будет запускать остальные 
5.1 вести лог слов и игроков и если что выдавать  сообщение (вынесть в отдельну ф-ю?)
6. Подключить код в бота
7. Бот должен прослушивать команду начала и завершения игры 
8. Реализовать сводку по команде или как-то еще

"""
import string
import csv
import random 
from random import randint


def city_list():
    city = []
    with open('geo.csv', mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f, delimiter=',')  
        for n, row in enumerate(reader):
            if not n:#skip header
                continue
            city.append(row['city']) 
    return city


# Инициальзация игры
def start_game(stop = False, users_list = None):
    if not users_list:
        users_list = []
        while True:
            user_bot = input("С вами будет играть бот? \nНапишите 'Да' или 'Нет': ")
            if user_bot == "Да":
                users_list.append("is_user_bot")
            elif user_bot != "Нет":
                print("Не известная команда, попробуйте еще раз\n")
                continue
            print("Напишите в чат кто будет играть:\n Напишите 'Стоп' когда закончите\n")
           
            i = 1
            while True:
                player_name_or_stop = input(f"Игрок №{i} ")
                if player_name_or_stop == 'Стоп':
                    random.shuffle(users_list,random.random)
                    print("\nПорядок игроков следующий:")
                    for user in range(len(users_list)):
                        print(f"{user + 1}. {users_list[user]}")
                    return users_list
                users_list.append(player_name_or_stop)
                i += 1


def game_master():
    users_list = start_game()
    word_log = dict()
    letter = random.choice("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ")
    word_log[letter] = set()
    raund = 1
    while True:
        print(f"Raund {raund}")
        for user in users_list:
            if letter not in word_log:
                word_log[letter] = set()
            if letter in "ЬЫЪЙЬ":
                print(f"На {letter} сложно найти город, сейчас найдем случайную букву")
                letter = random.choice("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ")
                
            print(f"Игроку {user} на букву {letter}")

            city_name = user_turn(user, letter, word_log)
            print(f"Слово {city_name} зачтено!")
            word_log[letter].add(city_name)
            letter = city_name[-1].upper()
        raund += 1
        

def user_turn(user, letter, word_log):
    if user == "is_user_bot":
        for city_name in city_list():
            if city_name[0] == letter: 
                if city_name[0] not in word_log: 
                    print(f"Бот отвечает {city_name}")
                    return city_name
                if city_name not in word_log[letter]:
                    print(f"Бот отвечает {city_name}")
                    return city_name
    while True:
        city_name = input(" Введите город : ")
        if city_name in city_list(): 
            if city_name[0] == letter: 
                if city_name[0] not in word_log: 
                    return city_name
                if city_name not in word_log[letter]:
                    return city_name
                print(f"Город {city_name} уже назывался, придумайте другой город на {letter}")
                continue
            print(f"Такой город существует но он начинается не на {letter}")
            continue
        print("Я не знаю такого города, попробуй ввести другой город")


game_master()