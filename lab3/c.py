#functuions1
#1

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("Введите количество граммов: "))
print(grams, "граммов =", round(grams_to_ounces(grams), 2), "унций")

#2

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input("Введите температуру в Фаренгейтах: "))
print(fahrenheit, "Фаренгейт =", round(fahrenheit_to_celsius(fahrenheit), 2), "Цельсий")


#3

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return None

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result:
    print("Курицы:", result[0], "Кролики:", result[1])
else:
    print("Решение не найдено")


#functions2

#1

def is_high_rated(movie):
    return movie.get('imdb', 0) > 5.5

movie = {'title': 'Inception', 'imdb': 8.8}
print(is_high_rated(movie))

#2

def is_high_rated(movie):
    return movie.get('imdb', 0) > 5.5

def filter_high_rated(movies):
    return [movie for movie in movies if is_high_rated(movie)]

movies = [
    {'title': 'Inception', 'imdb': 8.8},
    {'title': 'Movie A', 'imdb': 5.0},
    {'title': 'Movie B', 'imdb': 6.1}
]

print(filter_high_rated(movies))

#3

def is_high_rated(movie):
    return movie.get('imdb', 0) > 5.5

def filter_high_rated(movies):
    return [movie for movie in movies if is_high_rated(movie)]

def filter_by_category(movies, category):
    return [movie for movie in movies if movie.get('category') == category]

movies = [
    {'title': 'Inception', 'imdb': 8.8, 'category': 'Sci-Fi'},
    {'title': 'Movie A', 'imdb': 5.0, 'category': 'Drama'},
    {'title': 'Movie B', 'imdb': 6.1, 'category': 'Sci-Fi'}
]

print(filter_high_rated(movies))
print(filter_by_category(movies, 'Sci-Fi'))

#classes

#1

class StringProcessor:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Введите строку: ")
    
    def printString(self):
        print(self.string.upper())

processor = StringProcessor()
processor.getString()
processor.printString()

#2

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

square = Square(5)
print("Площадь квадрата:", square.area())

#3

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width




