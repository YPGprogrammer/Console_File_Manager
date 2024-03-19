import math

# Тест для функции filter:


def odd_num_filter():
    nums = [0, 2, 4, 10, 60, 52, 1, 3]
    out = filter(lambda n: n % 2 == 0, nums)
    return list(out)


def test_filter():
    assert odd_num_filter() == [0, 2, 4, 10, 60, 52]


# Тест для функции map:


def my_map_func():
    li = [1, 2, 3, 4, 5, 6]
    out = map(lambda x: x*2, li)
    return list(out)


def test_map():
    assert my_map_func() == [2, 4, 6, 8, 10, 12]


# Тест для функции sorted():


def my_sort_func():
    words = 'I love Python!'
    out = sorted(words)
    return out


def test_sorted():
    assert my_sort_func() == [' ', ' ', '!', 'I', 'P', 'e', 'h', 'l', 'n', 'o', 'o', 't', 'v', 'y']


# Тест для math.pi
def test_pi():
    assert math.pi == 3.141592653589793


# Тест для math.sqrt
def test_sqrt():
    assert math.sqrt(144) == 12


# Тест для math.pow
def test_pow():
    assert math.pow(3, 6) == 729


# Тест для path.hypot
def test_hypot():
    assert math.hypot(10, 12) == 15.620499351813308
