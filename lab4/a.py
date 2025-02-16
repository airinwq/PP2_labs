#date

#1
from datetime import date, timedelta
today = date.today()
print("Today:", today)
new = today - timedelta(days = 5)
print("after 5 days ", new)

#2
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3
from datetime import datetime
now = datetime.now()
without = now.replace(microsecond = 0)
print("With:", now)
print("Without:", without)


#4
from datetime import datetime
def in_seconds(d1, d2):
    format = "%Y-%m-%d %H:%M:%S"
    dt1 = datetime.strptime(d1, format)
    dt2 = datetime.strptime(d2, format)
    difference = abs((dt2 - dt1).total_seconds())
    return difference

d1 = input("first date: ")
d2 = input("second date: ")

diff = in_seconds(d1, d2)
print(f"Difference {diff} seconds")

#generators

#1
def gen_sq(n):
    for i in range(n + 1):
        yield i*i
n = int(input())
print("squares:")
for i in gen_sq(n):
    print(i)


#2
def even(k):
    for i in range(1,k + 1):
        if i % 2 == 0:
            yield i
k = int(input())
print("even:")
for i in even(k):
    print(i)


#3
def div(a):
    for i in range(0, a + 1):
        if i % 4 == 0 and i % 3 == 0:
            yield i
a = int(input())
print("nums divisible by 3 and 4:")
for i in div(a):
    print(i)


#4
def area_square(a,b):
    for i in range(a, b + 1):
        yield i **2

a = int(input("between "))
b = int(input("and "))
for i in area_square(a, b):
    print(i)


#5
def down(l):
    while l >= 0:
        yield l
        l -= 1
l = int(input())
print(f"from:{l} to 0 ")
for i in down(l):
    print(i)

#math

import math
#1
d = int(input("degree: "))
r = d * math.pi / 180
print("radian: ", r)


#2
h = int(input("height: "))
f = int(input("first value:"))
s = int(input("second value:"))
a = (f + s)*0.5*h
print("area", a)

#3
s = int(input("sides: "))
l = int(input("length: "))
area = (s * (l**2) * (1/math.tan(math.pi / s))) / 4 
print("area", int(area))

#4
l = int(input("Length of base:"))
h = int(input("Height of parallelogram:"))
ap = l*h
print ("area of the parallelogram: ", float(ap))




