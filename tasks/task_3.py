# Нужно найти среднее значение этих чисел и
# округлить его до одного знака после запятой
numbers: list = [12, 45, 0.34711, 67, 89, 34, 55.632781, 78.9395]

spread: float = sum(numbers) / len(numbers)

print(round(spread, 1))
