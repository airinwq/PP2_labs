#builtin
# #1
# import math
# def mult(li):
#     summa = math.prod(li)
#     print(summa)
# li = list(map(int, input().split()))
# mult(li)

# #2
# def countt(text):
#     upper = sum(1 for a in text if a.isupper())
#     lower = sum(1 for a in text if a.islower())
#     print(f"lower case letters:{lower}")
#     print(f"upper case letters:{upper}")
# text = input()
# countt(text)

# #3
# def palin(word):
#     return word == ''.join(reversed(word))
# word = input()
# if palin(word):
#     print("yes")
# else:
#     print("no")

# #4
# import time
# def square(a):
#     return math.sqrt(a)
# a = int(input())
# b = int(input())
# time.sleep(b/1000)
# squa = square(a)
# print(f"Square root of {a} after {b} miliseconds is {squa}")

# #5
# def istrue(tup):
#     return all(tup)
# tup = tuple(input().split())
# print(istrue(tup))
# if istrue(tup):
#     print(True)
# else:
#     print(False)