# Необходимо найти сумму всех элементов списка,
# а также определить максимальный и минимальный элементы.
numbers: list = [17, 6.06534, 91, 52, 87, 340, 56]

# Неправильная аннотация типа у переменных
sum_numbers: list = sum(numbers)
max_numbers: list = max(numbers)
min_numbers: list = min(numbers)

print('Сумма элементов списка:', sum_numbers)
print('Максимальный элемент списка:', max_numbers)
print('Минимальный элемент списка:', min_numbers)
