## 5. Основы коллекций в Python

_Важно! В данной теме мы рассмотрим стандартные типы данных поверхностно. В последующих темах углубимся в каждый из них
и рассмотрим их особенности и возможности более подробно._

![img.png](img%2Fimg.png)

Коллекции представляют собой важный инструмент при работе с данными. Они позволяют организовывать, хранить и
манипулировать группами элементов.

Добро пожаловать в тему коллекций в Python!

В этой теме познакомитесь с различными типами коллекций, которые Python предлагает: списки, кортежи, множества и
словари.

Начнем с основных концепций списков, затем перейдем к изучению кортежей, после чего рассмотрим множества и погрузимся
в мир словарей. Рассмотрим преобразование типов данных и ознакомимся с встроенными функциями Python,
которые широко используются при работе с коллекциями и числами.

- [Список](#список)
- [Кортеж](#кортеж)
- [Множество](#множество)
- [Словарь](#словарь)
- [Встроенные функции Python: преобразование типов данных часть 2](#встроенные-функции-python-преобразование-типов-данных-часть-2)
- [Встроенные функции Python: для работы с коллекциями и числами](#встроенные-функции-python-для-работы-с-коллекциями-и-числами)

---

### Список

Список `list()` представляет собой упорядоченную изменяемую последовательность элементов.

Список определяется с использованием квадратных скобок `[]`. Элементы списка разделяются запятыми.
Например, `[1.8, -15, 918]` - это список с тремя элементами.

**Создание пустого списка:**

* С помощью квадратных скобок

```python
empty_list = []
print(empty_list)  # []
```

* С использованием функции `list()`

```python
empty_list_2 = list()
print(empty_list_2)  # []
```

**Создание списка с данными:**

* С помощью квадратных скобок

```python
numbers = [10, 20, 30]
print(numbers)  # [10, 20, 30]
```

* С использованием функции `list()`

```python
chars = list("abc")
print(chars)  # ["a", "b", "c"]
```

Определение типа переменных с помощью функции `type()`

```python
print(type(numbers))  # <class 'list'>
print(type(chars))  # <class 'list'>
```

**Примеры создания и использования списка:**

```python
nums = [10, 20, 30, 40, 50]

# Доступ к элементу по положительному индексу
first_element = nums[0]  # 10

# Доступ к элементу по отрицательному индексу
last_element = nums[-1]  # 50

# Изменение значения элемента
nums[2] = 100  # [10, 20, 100, 40, 50]

# Добавление нового элемента в конец списка
nums.append(60)  # [10, 20, 100, 40, 50, 60]

# Удаление элемента по индексу
del nums[3]  # [10, 20, 100, 50, 60]

# Проверка наличия элемента в списке
is_present = 100 in nums  # True

print(nums)  # [10, 20, 100, 50, 60]
print(first_element)  # 10
print(last_element)  # 50
print(is_present)  # True
```

Списки могут содержать элементы разных типов, включая числа, строки, списки и другие объекты. Они являются универсальным
и гибким инструментом для хранения и обработки коллекций данных.

Основное отличие списка от других типов данных заключается в его изменяемости.
Список позволяет добавлять, изменять и удалять элементы, что делает его удобным для работы с изменяющимися данными.

---

### Кортеж

Кортеж `tuple()` представляет собой упорядоченную неизменяемую коллекцию элементов.

Кортеж определяется с использованием круглых скобок `()`. Элементы кортежа разделяются запятыми.
Например, `(145.7, -315, 10)` - это кортеж с тремя элементами.

**Создание пустого кортежа:**

* С помощью круглых скобок

```python
empty_tuple = ()
print(empty_tuple)  # ()
```

* С использованием функции `tuple()`

```python
empty_tuple_2 = tuple()
print(empty_tuple_2)  # ()
```

**Создание кортежа с данными:**

* С помощью круглых скобок

```python
nums = (3.1415, 12, 25)
```

* С использованием функции `tuple()`

```python
chars = tuple("abc")
print(chars)  # ("a", "b", "c")
```

Если необходимо создать кортеж с одним элементом, нужно добавить запятую после элемента.

* Создание кортежа с одним элементом

```python
single_element_tuple = ("Developer",)
print(single_element_tuple)  # ("Developer",)
```

Определение типа переменных с помощью функции `type()`

```python
print(type(nums))  # <class 'tuple'>
print(type(chars))  # <class 'tuple'>
print(type(single_element_tuple))  # <class 'tuple'>
```

**Примеры создания и использования кортежа:**

```python
mix_items = (1991, "Guido van Rossum", True, 6.28, 365)

# Доступ к элементу по положительному индексу
first_element = mix_items[0]  # 1991

# Доступ к элементу по отрицательному индексу
last_element = mix_items[-1]  # 365

# Проверка наличия элемента в кортеже
is_present = 6.28 in mix_items  # True

print(mix_items)  # (1991, "Guido van Rossum", True, 6.28, 365)
print(first_element)  # 1991
print(last_element)  # 365
print(is_present)  # True
```

Основное отличие кортежа от списка заключается в его неизменяемости.
Кортеж не позволяет добавлять, изменять или удалять элементы после создания.
Они также могут содержать элементы разных типов, таких как числа, строки и другие объекты.

Кортежи широко применяются для хранения наборов значений, которые остаются неизменными.
Например: координаты, константы или элементы, которые должны быть защищены от изменений.

---

### Множество

Множество `set()` представляет собой неупорядоченную коллекцию уникальных элементов.

Множество определяется с использованием фигурных скобок `{}` (только не пустое).
Элементы множества разделяются запятыми.
Например, `{0.145, -52, 3900}` - это множество с тремя элементами.

**Создание пустого множества:**

Пустое множество можно создать только с помощью функции `set()`

```python
empty_set = set()
print(empty_set)  # set()
```

Важно! Использование фигурных скобок `{}` не создает пустое множество. После изучения раздела о
словарях станет понятно, почему нельзя создать пустое множество с помощью фигурных скобок `{}`.

**Создание множества с данными:**

* С помощью фигурных скобок

```python
nums = {1.1, -432.52, 890}
print(nums)  # Выводит что-то вроде этого {-432.52, 1.1, 890}

# При выводе у вас может быть другой порядок элементов
```

* С использованием функции `set()`

```python
chars = set("abba")
print(chars)  # Выводит что-то вроде этого {"b", "a"}

# Повторяющиеся элементы игнорируются
```

**Отличия между `set()` и `frozenset()`**

В Python существует два типа множеств - изменяемое множество `set()` и неизменяемое множество `frozenset()`.

Основные их отличия:

* `set()` - можно изменять, добавлять и удалять элементы после создания.
* `frozenset()` - является неизменяемым, то есть его элементы не могут быть изменены или добавлены после создания.

**Примеры создания и использования множества:**

```python
nums = {10, 20, 30, 30, 40, 50, 40}  # {10, 20, 30, 40, 50}

# Добавление элемента в множество
nums.add(60)  # {10, 20, 30, 40, 50, 60}

# Удаление элемента из множества
nums.remove(20)  # {10, 30, 40, 50, 60}

# Добавление элемента в множество
nums.add(30)  # будет игнорироваться, так как элемент уже существует

print(nums)  # {10, 30, 40, 50, 60}

# Проверка наличия элемента в множестве
print(30 in nums)  # True

# Создание неизменяемого множества
fs_nums = frozenset([11, 22, 33])

print(fs_nums)  # frozenset({11, 22, 33})
```

Определение типа переменных с помощью функции `type()`

```python
print(type(nums))  # <class 'set'>
print(type(fs_nums))  # <class 'frozenset'>
```

Множества широко применяются для операций над уникальными значениями, удаления дубликатов, проверки принадлежности
элемента к множеству и выполнения операций над множествами.
Они предоставляют удобные методы для объединения множеств, нахождения их пересечения или разности.

Важно отметить, что множества могут содержать только элементы хешируемых типов (то есть неизменяемых типов данных).
Это означает, что списки и другие множества не могут быть элементами множества, но строки, числа и кортежи
могут использоваться как элементы множества.

---

### Словарь

Словарь `dict()` представляет собой упорядоченную коллекцию пар `{ключ: значение}`.

Ключи в словаре должны быть уникальными и неизменяемыми (например, строки, числа или кортежи).
Значения могут быть любого типа данных.

_Важно: До Python 3.6 версии словари не сохраняли порядок элементов, начиная с Python 3.7, официально
упорядочены. Это означает, что при переборе элементов порядок будет соответствовать порядку их добавления._

Словарь также определяется с использованием фигурных скобок `{}`, но в паре ключ-значение. Каждая пара разделяется
двоеточием, а элементы словаря разделяются запятыми. Например, `{'name': 'Иван', 'age': 18}` - это словарь с двумя
парами
ключ-значение.

**Создание пустого словаря:**

* С помощью фигурных скобок

```python
empty_dict = {}
print(empty_dict)  # {}
```

* С помощью функции `dict()`

```python
empty_dict_2 = dict()
print(empty_dict_2)  # {}
```

**Создание словаря с данными:**

* С помощью фигурных скобок

```python
employee_info = {
    "name": "Максим",
    "age": 23,
    "city": "Москва",
    109465: "Идентификатор для примера",
    (10, 10, 10): "Кортеж можно использовать в качестве ключа"
}
```

* С помощью функции `dict()`

```python
fruits_count = dict([('apple', 10), ('banana', 20), ('orange', 30)])
print(fruits_count)  # {'apple': 10, 'banana': 20, 'orange': 30}
```

В примере выше в функцию `dict()` передается список кортежей, где каждый кортеж содержит два элемента: первый элемент -
это ключ, а второй элемент - это значение.

* Ключ `'apple'` со значением `10`
* Ключ `'banana'` со значением `20`
* Ключ `'orange'` со значением `30`

```python
person = dict(name="Екатерина", age=18, city="Санкт-Петербург", position="SEO Manager")
print(person)  # {'name': 'Екатерина', 'age': 18, 'city': 'Санкт-Петербург', 'position': 'SEO Manager'}
```

В данном случае, вместо передачи списка кортежей, используется нотация `ключ=значение` для определения элементов
словаря.

* Ключ `'name'` со значением `'Екатерина'`
* Ключ `'age'` со значением `18`
* Ключ `'city'` со значением `'Санкт-Петербург'`
* Ключ `'position'` со значением `'SEO Manager'`

**Примеры создания и использования словаря:**

```python
person_data = {'name': 'Алексей', 'age': 25, 'city': 'Москва'}

# Доступ к значению по ключу
print(person_data['name'])  # 'Алексей'

# Изменение значения по ключу
person_data['age'] = 30

# Добавление новой пары ключ-значение
person_data['occupation'] = 'Инженер'

print(person_data)  # {'name': 'Алексей', 'age': 30, 'city': 'Москва', 'occupation': 'Инженер'}

# Проверка наличия ключа в словаре
print('city' in person_data)  # True

print(type(person_data))  # <class 'dict'>
```

Основное отличие словаря от других типов данных заключается в том, что словарь использует ключи для доступа к
своим значениям, в то время как остальные типы данных используют целочисленные индексы.

Словари широко применяются для хранения и доступа к данным по уникальным ключам. Они удобны для представления
структурированной информации и находят применение в различных алгоритмах, а также при работе с базами данных или
настройке приложений.

---

### Встроенные функции Python: преобразование типов данных часть 2

В этом разделе мы продолжим изучение встроенных функций преобразования типов данных в Python. В первой части мы уже
познакомились с базовыми функциями, такими как `int()`, `float()` и `str()`. Теперь перейдем к рассмотрению
дополнительных способов преобразования типов данных, включая списки, кортежи, множества и словари.

**Примеры преобразования различных типов данных с использованием функции `list()`:**

* Преобразование строки в список

```python
string = "Hello, World!"
string_list = list(string)
print(string_list)  # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
```

* Преобразование кортежа в список

```python
tuple_data = (1, 2, 3, 4, 5)
tuple_list = list(tuple_data)
print(tuple_list)  # [1, 2, 3, 4, 5]
```

* Преобразование множества в список

```python
set_data = {1, 2, 3, 4, 5}
set_list = list(set_data)
print(set_list)  # [1, 2, 3, 4, 5]
```

Важно: Числа не могут быть преобразованы напрямую с помощью `list()`.
Если вам необходимо создать список чисел, можете использовать квадратные скобки и
разделять элементы запятыми, например: `number_list = [1, 2, 3, 4, 5]`.

**Примеры преобразования различных типов данных в кортеж с использованием функции `tuple()`:**

* Преобразование строки в кортеж

```python
string = "Hello, World!"
tuple_data = tuple(string)
print(tuple_data)  # ('H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!')
```

* Преобразование списка в кортеж

```python
list_data = [1, 2, 3, 4, 5]
tuple_data = tuple(list_data)
print(tuple_data)  # (1, 2, 3, 4, 5)
```

* Преобразование множества в кортеж

```python
set_data = {1, 2, 3, 4, 5}
tuple_data = tuple(set_data)
print(tuple_data)  # (1, 2, 3, 4, 5)
```

Также как в примеры со списками, числа не могут быть преобразованы напрямую с помощью `tuple()`.
Если вам необходимо создать кортеж чисел, можете использовать круглые скобки и разделять элементы
запятыми, например: `number_tuple = (1, 2, 3, 4, 5)`.

**Примеры преобразования различных типов данных в множество с использованием функций `set()` и `frozenset()`:**

Преобразование строки в множество с использованием `set()` и `frozenset()`

```python
string = "Hello, World!"
set_data = set(string)
print(set_data)  # {'!', 'r', 'H', ' ', 'l', 'o', 'd', 'e', 'W', ','}

string_2 = "Hello, World!"
frozen_set_data = frozenset(string_2)
print(frozen_set_data)  # frozenset({'o', 'd', ',', 'H', ' ', 'r', '!', 'l', 'W', 'e'})
```

* Преобразование списка в множество с использованием `set()` и `frozenset()`

```python
list_data = [1, 2, 3, 3, 4, 4, 5]
set_data = set(list_data)
print(set_data)  # {1, 2, 3, 4, 5}

list_data_2 = [1, 2, 3, 3, 4, 4, 5]
frozen_set_data = frozenset(list_data_2)
print(frozen_set_data)  # frozenset({1, 2, 3, 4, 5})
```

* Преобразование кортежа в множество с использованием `set()` и `frozenset()`

```python
tuple_data = (1, 2, 2, 3, 4, 4, 5)
set_data = set(tuple_data)
print(set_data)  # {1, 2, 3, 4, 5}

tuple_data_2 = (1, 2, 2, 3, 4, 4, 5)
frozen_set_data = frozenset(tuple_data_2)
print(frozen_set_data)  # frozenset({1, 2, 3, 4, 5})
```

При преобразовании в множество `set()` все дубликаты удаляются, так как множество содержит только уникальные элементы. В
случае `frozenset()`, который является неизменяемым, также удаляются дубликаты.

---

### Встроенные функции Python: для работы с коллекциями и числами

Python предлагает множество полезных встроенных функций, которые облегчают работу с коллекциями и числами. Эти функции
позволяют выполнять различные операции, такие как подсчет суммы элементов, поиск максимального и минимального значения,
определение длины коллекции, проверка условий и др.

Рассмотрим некоторые из них:

**Функция `len()`**

Функция `len()` используется для определения длины коллекции, то есть количества элементов в ней. Например,

* Строки

```python
string = "Hello, World!"
print(len(string))  # 13

# возвращает количество символов в строке.
```

* Списки

```python
nums = [10, 22, 52, -164, 1.87]
print(len(nums))  # 5

# возвращает количество элементов в списке.
```

* Кортежи

```python
mix_items = (0.3471, -472, 133, "Hello World", True)
print(len(mix_items))  # 5

# возвращает количество элементов в кортеже.
```

* Множества

```python
numbers = {1, 2, 3, 4, 5}
print(len(numbers))  # 5

# возвращает количество элементов в множестве.
```

* Словари

```python
fruits = {'apple': 23, 'banana': 125, 'orange': 287}
print(len(fruits))  # 3

# возвращает количество пар ключ-значение в словаре. 
# В данном примере словарь содержит 3 пары ключ-значение.
```

**Функция `abs()`**

Используется для получения абсолютного значения числа.
Абсолютное значение представляет собой числовое значение без учета его знака, то есть всегда положительное значение.

```python
number = -5
absolute_value = abs(number)
print(absolute_value)  # 5
```

**Функция `sum()`**

Применяется только к коллекциям чисел (спискам, кортежам и множествам) и выполняет операцию суммирования их элементов.

Например:

```python
nums_list = [11, 12, 4.3, 40, 15]
print(sum(nums_list))  # 82.3

nums_tuple = (10, 20, 30, -40, 50)
print(sum(nums_tuple))  # 70

numbers_set = {1, 2, 3, 4, 5}
print(sum(numbers_set))  # 15
```

**Функции `round()` и `pow()`**

* `round()` используется для округления числа до указанного количества знаков после запятой.
* `pow`() используется для возведения числа в степень.

```python
# round
number = 3, 1415926535
result = round(number, 2)
print(result)  # 3.14

# pow
base = 2
exponent = 3
print(pow(base, exponent))  # 8

# функцию pow() можно заменить оператором **(возведение в степень)
```

**Функции `min()` и `max()`**

- `min()` возвращает наименьший элемент из коллекции или последовательности чисел.
- `max()` возвращает наибольший элемент из коллекции или последовательности чисел.

```python
numbers = [15, 2, 4, 1, -9]
mn = min(numbers)
mx = max(numbers)

print(mn)  # -9
print(mx)  # 15

chars = ['a', 'c', 'b', 'z', 'f']
mn_ch = min(chars)
mx_ch = max(chars)

print(mn_ch)  # a
print(mx_ch)  # z

text = "Hello, World!"

mn_t = min(text)
mx_t = max(text)
print(mn_t)  # ' '
print(mx_t)  # 'r'
```

Эти функции для строк и коллекций символов определяют минимальный и максимальный символ на основе их порядка в таблице
символов [Unicode](https://en.wikipedia.org/wiki/List_of_Unicode_characters).

Каждый символ имеет свой уникальный числовой код в этой таблице, и функции `min()` и `max()` сравнивают
эти числовые коды для определения наименьшего и наибольшего символа.
Порядок символов в таблице `Unicode` определен стандартом.

Важно отметить, что при использовании функций `min()` и `max()` с коллекциями (списки, кортежи и т.д.), содержащими
элементы разных типов (строки, числа и т.д.), может возникнуть ошибка.
Это связано с тем, что элементы должны быть сравнимы между собой, чтобы определить минимальный и максимальный элемент.

```python
elements = [1, 'apple', True, 3.14, 'banana']

mn = min(elements)  # TypeError: '<' not supported between instances of 'str' and 'int'
print(mn)

mx = max(elements)  # TypeError: '>' not supported between instances of 'str' and 'int'
print(mx)
```

Если в коллекции встречаются несравнимые типы как в примере выше, функции `min()` и `max()` вызовут
исключение `TypeError`. Для успешного использования этих функций необходимо убедиться,
что элементы коллекции сравнимы между собой.

**Функции `all()` и `any()`**

Функции `all()` и `any()` являются полезными инструментами для работы с коллекциями. Они позволяют проверять, являются
ли элементы коллекции истинными или ложными значениями.

Функция `all()` принимает коллекцию (список, кортеж, множество) в качестве аргумента и возвращает `True`, если
все элементы коллекции являются истинными значениями. Если же в коллекции есть хотя бы один ложный элемент,
функция `all()` вернет `False`.

**Важно:** Если коллекция пуста, функция `all()` также вернет `True`.

* Пример использования функции `all()`:

```python
# все элементы списка являются истинными значениями
mix_1 = [10, "Hello", [1, 2, 3]]
result_1 = all(mix_1)
print(result_1)  # True

# есть хотя бы один ложный элемент в списке
mix_2 = [5, "Oops!", (), 100]
result_2 = all(mix_2)
print(result_2)  # False

# пустой список
empty = []
result_3 = all(empty)
print(result_3)  # True
```

Функция `any()` работает аналогично, но возвращает `True`, если в коллекции есть хотя бы один истинный элемент.
Если все элементы коллекции являются ложными значениями или коллекция пуста, функция `any()` вернет `False`.

* Пример использования функции `any()`:

```python
# есть хотя бы один истинный элемент в списке
mix_1 = [0, "", (), "Hello"]
result_1 = any(mix_1)
print(result_1)  # True

# все элементы списка являются ложными значениями
mix_2 = [False, "", 0, ()]
result_2 = any(mix_2)
print(result_2)  # False

# пустой список
empty = []
result_3 = any(empty)
print(result_3)  # False
```

Важно отметить, что функции `all()` и `any()` могут работать только с элементами, которые могут быть интерпретированы
как логические значения (истина или ложь). Если в коллекции присутствуют элементы других типов для которых это не
применимо, результат может быть непредсказуемым.

---

В этой теме познакомились с основами коллекций в Python. Рассмотрели различные типы коллекций,
и узнали, как они могут быть использованы для организации, хранения и манипуляции группами элементов.

Теперь у вас есть фундаментальное понимание коллекций и умение работать с ними.
Это является важной основой для эффективного использования и обработки данных в вашем коде.
В следующих темах углубимся в каждый тип коллекций, рассмотрим их особенности и возможности более подробно.

В следующей теме перейдем к рассмотрению условных операторов. Готовьтесь к новому уровню владения Python!

---

### [Задания](./tasks/TASKS.md)
