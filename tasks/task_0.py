# Нужно поменять местами первый и последний элементы этого списка
colors: list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

colors[-1], colors[0] = colors[0], colors[-1]

print(colors)
