# Examples of different ways to filter data
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# All positive values
pos = [n for n in mylist if n > 0]
print(pos)

# All negative values
neg = [n for n in mylist if n < 0]
print(neg)

# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
print(neg_clip)

# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print(pos_clip)

# Compressing example

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
a = list(compress(addresses, more5))
print(a)


class Apple:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def __repr__(self):
        return 'Apple [name = {}, color = {}]'.format(self.__name, self.__color)

    def map_to_my_apple(self):
        return MyApple(self.color, self.name)


class MyApple:
    def __init__(self, name=None, color=None):
        self.__name = name
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def __repr__(self):
        return 'MyApple [name = {}, color = {}]'.format(self.__name, self.__color)


def map_apple_to_my_apple(apple):
    return MyApple(apple.color, apple.name)


apple_list = [Apple('a', 'Red'), Apple('b', 'Green'), Apple('c', 'Blue')]
print(apple_list)

apple_color_list = [apple.color for apple in apple_list]
print(apple_color_list)

apple_name_list = [apple.name for apple in apple_list]
print(apple_name_list)

my_apple_list = [map_apple_to_my_apple(apple) for apple in apple_list]
print(my_apple_list)

my_apple_list = [apple.map_to_my_apple() for apple in apple_list]
print(my_apple_list)