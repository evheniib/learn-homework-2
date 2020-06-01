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
import csv
import random 
from random import randint

# Инициальзация игры
def start_game(stop = False, users_list = None):
    if not users_list:
        users_list = []
        while True:
            user_bot = input("С вами будет играть бот? \nНапишите 'Да' или 'Нет': ")
            if user_bot == "Да":
                users_list.append("Bot")
            elif user_bot != "Да" and user_bot != "Нет":
                print("Не известная команда, попробуйте еще раз\n")
                continue
            print("Напишите в чат кто будет играть:\n Напишите 'Стоп' когда закончите\n")
           
            i = 1
            while True:
                amount = input(f"Игрок №{i} ")
                if amount == 'Стоп':
                    random.shuffle(users_list,random.random)
                    print("\nПорядок игроков следующий:")
                    for user in range(len(users_list)):
                        print(f"{user + 1}. {users_list[user]}")
                    return users_list
                users_list.append(amount)
                i += 1


""" 
1. Хочу разработать пуск игры по очереди используя функцию user_turn(user, oponent_word = None), 
2. Тот кто ходит первый идет без проверки предыдущего слова.
3. Запись слов будет идти в список словарей, где в словаре {'Слово':'Игрок'} 
4. Текущая функция должна проверять проверять вернувшееся в нее слово от игрока
   и если все ок то добавляем пару Слово:Игрок в словарь.
5. Я не знаю на стороне какой функции лучше реализовать 
   проверку попадания первой буквы нового слова в последнию предыдущего
   game_master() или user_turn()

# Запускает игру останавливается когда user_turn передаст "Стоп"
def game_master():
    users_list = start_game()
    print(f"Да начнется игра! Первым ходит {users_list[0]}")
    word_log = [
        {None: None},
    ]
    turn = 0

    while True:
        if turn <= len(users_list):
            user_word = {}
            user_answer = user_turn(users_list[turn], word_log[-1].)
            user_word[user_answer] = users_list[turn]
            word_log.append(user_word)
            continue
        turn = 0
"""



def city_list():
    city = []
    with open('geo.csv', mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f, delimiter=',')  
        for n, row in enumerate(reader):
            if not n:#skip header
                continue
            city.append(row['city']) 
    return city


# Получение списка городов, возвращаем город который есть в csv файле
def user_turn(user, oponent_word = None):
    if not oponent_word:
        print(f"{user} first!")
    #Если бот   
    if user == 'Bot':
        if oponent_word:
            for city_name in city_list():
                if oponent_word[-1].upper() == city_name[0]:
                    send_city(city_name, "Bot")
                    return user_turn(city_name)           
        city_name = random.choice(city_list())
        send_city(city_name, "Bot`s")
        return user_turn(city_name)
    #Если игрок  
    if oponent_word:
        while True:
            city_name = input(" Введите город : ")
            if city_name in city_list():
                return send_city(city_name)
            print("Я не знаю такого города, попробуй ввести другой город")
    

def send_city(city_name, user):
    print(f"{user} назвал город {city_name} следущий игрок начинает на букву {city_name[-1].upper()}")
    return city_name

start_game()

