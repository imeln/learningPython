print([1, 2, 3] + ['A', 'B', 'C'])  # С помощью оператора + можно объединить два списка в новый список. Конкатенация
print(['X', 'Y', 'Z'] * 3)  # Умножая список с помощью оператора * на целое число, можно повторить список заданное
# количество раз. Репликация

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]  # Инструкцией del удалить из списка значение с заданным индексом.
print(spam)  # Все значения, находящиеся после удаленного, сдвигаются к началу списка на одну позицию.
del spam[2]
print(spam)
