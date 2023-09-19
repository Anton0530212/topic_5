fruits: dict = dict(
    [
        ('яблоко', 50),
        ('банан', 30),
        ('груша', 40),
        ('апельсин', 35)
    ]
)

print('Список фруктов и их цены:\n', fruits, sep='', end='\n\n')

user_input: str = input('Выберите фрукт из списка: ')
price: dict = fruits[user_input]

print('Цена', user_input, '-', price)

# --------------------------------examples

# SELECT price FROM fruits;
# WHERE name == user_input;

# data_1 = [
#     ('apple', 10),
#     ('banana', 20),
#     ('orange', 30)
# ]
#
# print(dict(data_1))
#
#
# data_2 = dict(apple=10, banana=20, orange=30)
# data_3 = dict(яблоки=10, бананы=20, апельсины=30)
# print(data_2)
# print(data_3)
