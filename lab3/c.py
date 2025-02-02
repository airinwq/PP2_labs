#functuions1

#1

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input())
print(grams, round(grams_to_ounces(grams), 2))

#2

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input())
print(fahrenheit, round(fahrenheit_to_celsius(fahrenheit), 2))


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
    print(result[0], result[1])
else:
    print("Решение не найдено")

#4

def is_prime(nums):
    prime_list = []
    for i in nums:
        if i % 2 == 0:
            prime_list.append(i)
    return prime_list

entered_list = list(map(int, input("Enter numbers separated by space: ").split()))
print(is_prime(entered_list))

#5

from itertools import permutations

def print_permutations(s):
    perm_list = permutations(s)
    for perm in perm_list:
        print(''.join(perm))

user_input = input("Enter a string: ")
print_permutations(user_input)

#6

def rev_str(string):
    string.reverse()
    for word in string:
        print(word, end=" ")

list_str = input().split()
rev_str(list_str)

#7

def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] == 3 == nums[i]:
            return True
    return False

entered_list = list(map(int, input("Enter numbers separated by space: ").split()))
print(has_33(entered_list))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


#8

def spy_game(nums):
    spy = [x for x in nums if x == 0 or x == 7]
    for i in range(2, len(spy)):
        if spy[i - 2] == 0 == spy[i - 1] and spy[i] == 7:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#9


def volume_sphere(r):
    pi = 3.14
    print (round(4 / 3 * pi * r ** 3, 2))

radius = int(input("Radius: "))
volume_sphere(radius)

#10

def unique_elements(first_list):
    new_list = [first_list[0]]
    for item in first_list:
        if item not in new_list:
            new_list.append(item)
    print("New list without duplicates:", new_list)

enter_list = list(map(int, input("Enter numbers separated by space: ").split()))
unique_elements(enter_list)

#11

def polindrome(word):
    new_word = word[::-1]
    print("Polindrome" if new_word == word else "Not polindrome")

word = input("Enter word: ")
polindrome(word)

#12

def histogram(values):
    for i in values:
        for j in range(i):
            print("*", end="")
        print()

nums = list(map(int, input("Enter numbers separated by space: ").split()))
histogram(nums)

#13

import random as rand
def guess_num():
    name = input("Hello! What is your name?\n")

    rand_num = rand.randint(1, 20)

    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")

    i = 0
    num = 0
    while num != rand_num:
        num = int(input())
        i += 1

        if num < rand_num:
            print("Your guess is too low.\nTake a guess.")
        elif num > rand_num:
            print("Your guess is too high.\nTake a guess.")
        else:
            print(f"Good job, {name}! You guessed my number in {i} guesses!")

guess_num()


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

#4

def avg_imdb():
    sum = 0
    for movie in movies:
        sum += movie["imdb"]
    print (f"The average of IMDB: {sum / len(movies):.1f}")

avg_imdb()

#5

def avg_imdb_by_category(category):
    sum = 0
    cnt_movies = 0
    for movie in movies:
        if movie["category"] == category:
            sum += movie["imdb"]
            cnt_movies += 1
    print (f"The average of IMDB on category {category}: {sum / cnt_movies:.1f}")

category = input("Enter the category of movies: ")
avg_imdb_by_category(category)


#classes

#1

class StringProcessor:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input()
    
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
print(square.area())

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

#4

from math import sqrt

class Point:
    x0 = 0
    y0 = 0
    def __init__(self):
        self.x = int(input("x coordinate: "))
        self.y = int(input("y coordinate: "))

    def show(self):
        print(f"Point coordinates ({self.x}, {self.y})")

    def move(self):
        global x0, y0
        x0 = self.x
        y0 = self.y
        self.x = int(input("x coordinate: "))
        self.y = int(input("y coordinate: "))

    def dist(self):
        self.distance = sqrt((x0 - self.x) ** 2 + (y0 - self.y) ** 2)
        print("The distance between 2 points:", round(self.distance, 2))


point = Point()
point.show()
point.move()
point.dist()

#5

class Account:
    def __init__(self):
        self.owner = input("Enter your name: ")
        self.balance = float(input("Enter your balance: "))

    def deposit(self):
        amount = float(input("Deposit: "))
        self.balance += amount
        print("Your balance: ", self.balance, "\n")

    def withdraw(self):
        amount = float(input("Withdraw: "))
        if amount > self.balance:
            print("You can not exceed the available balance.")
        else:
            self.balance -= amount
        print("Your balance: ", self.balance, "\n")

acc = Account()
acc.deposit()
acc.withdraw()

#6

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filt_prime(nums):
    return list(filter(lambda x: is_prime(x), nums))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = filt_prime(numbers)
print("Prime numbers:", prime_numbers)






