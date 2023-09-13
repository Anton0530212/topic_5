# Программа которая сохдает множество,
# содержащее только ключи этого словаря,
# и выведите его на экран
student_info: dict = {"name": "Анна", "age": 20, "group_number": "А101"}

keys_set: set = set(student_info)

print(keys_set)
