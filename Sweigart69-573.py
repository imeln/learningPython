# Демонстрация работы инструкции else if - иногда желательно выбрать для выполнения один из нескольких блоков.

print('Введите ваше имя')
name = input()
print('Введите ваш возраст')
age = input()
age = int(age)
if name == 'Alice':  # Инструкция else if может помещаться только после инструкции if или другой инструкции elif.
    print('Привет, Элис.')
elif age < 12:  # Инструкция состоит иэ элементов 1) ключевое слово 2) условие - выражение с True или False 3) двоеточие
    print('Малыш, ты не Элис')  # 4) блока кода с отступом, начинающийся в следующей строке.
