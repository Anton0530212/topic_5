# Нужно поменять местами первый и последний элементы этого списка
colors: list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

# Неправильно, места надо менять, а не писать вручную
colors[0]: str = "Yellow"
colors[-1]: str = "Red"

print(colors)
