def summarize(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def get_dict():
    return {'name': 'Ivan', 'age': 29, 'city': 'Moscow'}


def get_list():
    return [1, 2, 3, 4]


def factorial(number: int) -> int:
    fact = 1
    if number < 0:
        raise ValueError('Cannot accept negative numbers')
    elif number == 0:
        return 1
    else:
        for i in range(1, number + 1):
            fact *= i
    return fact


NUMBER = 50

#assert
a = 10
b = 22
result = summarize(a, b)
expected = 32
assert result == expected


# x = 156
# y = 867
# result = summarize(x, y)
# expected = 1000
# assert result == expected

# is
dict1 = get_dict()
key = 'date_of_birth'
value = dict1.get(key)
assert value is None
key2 = 'city'
value2 = dict1.get(key2)
assert value2 is not None

# in
list1 = get_list()
val1 = 10
assert val1 not in list1


# операторы сравнения ==,!=,<,>,<=,>=
# оператор идентичности is, is not
# вхождение in, not in
# isinstance(), issubclass()
