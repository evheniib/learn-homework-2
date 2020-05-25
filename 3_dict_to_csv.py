"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
 В списке нужно создать не менее 4-х словарей                                           +
2. Запишите содержимое списка словарей в файл в формате csv                             +

"""
import csv

def main():
    
    staff = [
         {'Name': 'Петр', "age": 21, 'job': "Teacher", 'Salary': 334},
         {'Name': 'Миша', "age": 31, 'job': "Presidend", 'Salary': 10124},
         {'Name': 'Сара', "age": 29, 'job': "Soldier", 'Salary': 954},
         {'Name': 'Герман', "age": 24, 'job': "Artist", 'Salary': 124},
         {'Name': 'Евлампий', "age": 33, 'job': "Teacher", 'Salary': 744},
         {'Name': 'Феофан', "age": 50, 'job': "Nurse", 'Salary': 134},
         {'Name': 'Мефодий', "age": 27, 'job': "Doctor", 'Salary': 344},
    ]

    with open('staff.csv', 'w', encoding='utf-8') as f:
        fields = staff[0].keys()
        writer = csv.DictWriter(f, fields, delimiter = ';')
        writer.writeheader()
        for employee in staff:
            writer.writerow(employee)


if __name__ == "__main__":
    main()
