#Regex

import re
#1
enter = input("enter: ")
text = r"ab*"
match = re.findall(text, enter)
print("'a' followed by zero or more 'b''s")
print(match)

#2
enter = input("enter ")
text = r"ab{2,3}"
match = re.findall(text, enter)
print(match)

#3
enter = input("enter ")
text = r"[a-z]+(?:_[a-z]+)+"
match = re.findall(text, enter)
print(match)

#4
enter = input("enter ")
text = r"[A-Z][a-z]+"
match = re.findall(text, enter)
print(match)

#5
enter = input("enter ")
text = r"a.*b$"
match = re.findall(text, enter)
print(match)

#6
enter = input("enter ")
text = r",|/.|\s"
replaceto = ":"
match = re.sub(text, replaceto, enter)
print(match)

#7
enter = input("enter ")
mylist = re.split('_', enter)
text = mylist[0]
for i in range(1, len(mylist)):
    text += mylist[i].capitalize()
print(text)

#8
enter = input("enter ")
match = re.findall('[A-Z][a-z]+', enter)
print(match)

#9
enter = input("enter ")
match = re.sub('([a-z])([A-Z])', r'\1 \2', enter)
print(match)

#10
enter = input("enter ")
match = re.sub('([a-z])([A-Z])', r'\1 \2', enter)
match1 = re.sub(' ', r'_', match)
match2 = match1.lower()
print(match2)