# Для выполнения блока кода лишь определенное количество раз можно воспользоваться циклом for
# и функцией range().

print('Мое имя')
for i in range(5):  # Блок кода цикла for выполняется пять раз. На первой итерации значение переменной устанвливается 0
    print('Алексей пять раз (' + str(i) + ')')  # Когда завершена итерация, выполнен весь блок кода, управление
    # передается в начало цикла, где инструкция for увеличивает значение переменной i на единицу.

