# Программа, которая принимает строку и определяет
# минимальный и максимальный символы в ней.
line: str = input('Введите строку: ')

min_line: str = min(line)
max_line: str = max(line)

print('Минимальный символ:', min_line)
print('Максимальный символ:', max_line)
