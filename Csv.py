import random
import time
from transliterate import translit

# Пользователь вводит информацию о годе, факультете, группе и курсе
print("Введите год:")
year = input()
print("Введите факультет:")
dep = input()
print("Введите группу:")
group = input()
print("Введите курс:")
course = input()

start_time = time.time()  # Засекаем начальное время выполнения программы

# Открываем файл с фамилиями и именами студентов для чтения
with open("Students.txt", "r", encoding="utf-8") as file:
    # Открываем файл CSV для записи
    with open("students.csv", "w") as ofile:
        # Записываем заголовок CSV-файла
        ofile.write(';'.join(["username", "password", "first name", "last name", "email", "city", "maildisplay", "course", "group"]) + '\n')

        # Считываем все строки из файла с именами
        names = file.readlines()

        # Для каждой строки имени в файле
        for name in names:
            # Разбиваем строку на фамилию, имя и отчество
            lname, fname, mname = name.rstrip("\n").split()
            # Генерируем логин пользователя
            username = dep.lower() + group.lower() + year + translit(fname[0] + mname[0] + lname, "ru", reversed=True)
            # Генерируем пароль
            password = ''.join(random.choice("0123456789") for _ in range(4))
            # Генерируем электронную почту
            email = username + "@fiztest.gsu.by"
            # Записываем данные пользователя в файл CSV
            ofile.write(';'.join([username, password, fname + ' ' + mname, lname, email, "Гомель", "0", course, group]) + '\n')

print("Готово! Время выполнения:", time.time() - start_time, "секунд")