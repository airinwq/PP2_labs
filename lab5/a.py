#Regex

#1

import re

def match_pattern(string):
    pattern = r'^ab*$'  
    if re.fullmatch(pattern, string):
        return "Match found"
    else:
        return "No match"


test_strings = ["a", "ab", "abb", "abbb", "ac", "ba", "abc"]
for s in test_strings:
    print(f"'{s}': {match_pattern(s)}")

#2

import re

def match_pattern(string):
    pattern = r'^abb{2,3}$'  
    if re.fullmatch(pattern, string):
        return "Match found"
    else:
        return "No match"

test_strings = ["a", "ab", "abb", "abbb", "abbbb", "ac", "ba", "abc"]
for s in test_strings:
    print(f"'{s}': {match_pattern(s)}")

#3

import re

def match_pattern(string):
    pattern = r'^[a-z]+_[a-z]+$'  
    if re.fullmatch(pattern, string):
        return "Match found"
    else:
        return "No match"


test_strings = ["hello_world", "test_case", "no_match", "UPPER_CASE", "under_score_"]
for s in test_strings:
    print(f"'{s}': {match_pattern(s)}")

#4

import re

def match_pattern(string):
    pattern = r'^[A-Z][a-z]+$'  
    if re.fullmatch(pattern, string):
        return "Match found"
    else:
        return "No match"


test_strings = ["Hello", "Test", "noMatch", "UPPERCASE", "CamelCase"]
for s in test_strings:
    print(f"'{s}': {match_pattern(s)}")

#5

import re

def match_pattern(string):
    pattern = r'^a.*b$'  
    if re.fullmatch(pattern, string):
        return "Match found"
    else:
        return "No match"


test_strings = ["ab", "axb", "a123b", "a_b", "bba", "abc"]
for s in test_strings:
    print(f"'{s}': {match_pattern(s)}")


