# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]


def print_task_1(dict_values):
    for key in dict_values.keys():
        print (f"{key}: {dict_values[key]}")


def task_1(students):
    names_list = [students[i]['first_name'] for i in range(len(students))]
    uniqe_names = dict()
    for name in names_list:
        pos_counter = names_list.index(name) + 1
        if name not in uniqe_names:
            uniqe_names[name] = 1
        else:
            continue
        if pos_counter == len(names_list):
            break 
        for compared_name in names_list[pos_counter:]:
            if name == compared_name:
                uniqe_names[name] += 1 
    return uniqe_names   

print("\ntask_1")
print_task_1(task_1(students))

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]


def print_task2(dict_values):
    max_val = max(dict_values.values())
    for key in dict_values.keys():
        if dict_values[key] == max_val:
            print(f"Самое частое имя среди учеников: {key}")

print("\ntask_2")
print_task2(task_1(students))  


# Пример вывода:
# Самое частое имя среди учеников: Маша
 

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

print("\ntask_3")
print_task2(task_1(school_students[0]))
print_task2(task_1(school_students[1]))

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

    

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


def task_4(school, is_male):
    genders_in_grades = {}
    for grade in school:
        students = [grade["students"][i]['first_name'] for i in range(len(grade['students']))]
        count_boys = 0
        count_girls = 0
        for student in students:
            if is_male == student:
                count_boys += 1
            else:
                count_girls += 1
        genders_in_grades[grade['class']] =  [count_girls, count_boys]  
    return genders_in_grades

def print_task4(school):
    for grade in school.keys():
         print(f"В классе {grade} {school[grade][0]} девочки и {school[grade][1]} мальчика.")


print("\ntask_4")
print_task4(task_4(school, is_male))

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a