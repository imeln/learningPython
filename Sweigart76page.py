# Инструкция while для организации многократного выполнения блока кода, пока выполняется указанное условие.

print('Введите количество банок тушенки')
spam = input()
spam = int(spam)
while spam < 5:  # Использовать инструкцию while - цикл. Определить условие - выражение дающее True или False.
    print('Получите банку тушенки.')  # Проверим значение переменной, и если оно меньше 5, то выведем сообщение.
    spam = spam + 1  # По достижение конца блока кода цикла while управление передается в начало.