"""
INTRUCTIONS
You are given a string s of length n, with n ranging from 1 to 500 inclusive. This string represents the complex and jumbled record of a sports game. It combines player names and scores but lacks a uniform structure. The player names consist of words made up of lowercase English alphabets (a-z), while the scores are integers ranging from 1 to 100 inclusive.

Your mission involves writing a Python function solution(). This function should parse the given string, isolate the integers representing player scores, and return the sum of these scores.

For instance, for the input string, "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe", your function should return the sum 5 + 10 + 2 + 1, which totals 18.

======================================================================================================

THOUGTH PROCESS
    1. Split the string into a list of words
    2. Iterate the list verifying if the current word is a digit
    3. If it is a digit, add the number to a variable sum
    4. Return this variable

PROBLEMS DURING THE IMPLEMENTATION
    A digit can be follower by a comma, so we have to deal with this situation

    SOLUTION
        Iterate insite the word looking for digit numbers and join them into a string

    APPROACH PROBLEM
        This solution have O(n^2) complexity
"""

def solution(input_str):
    words = input_str.split()
    sum = 0
    
    for w in words:
        w = ''.join(c for c in w if c.isdigit())
        if w.isdigit():
            sum += int(w)

    return sum

print(solution("joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"))


