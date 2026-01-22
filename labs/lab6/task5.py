import string

def is_palindrome(s):
    clean = ""
    for ch in s.lower():
        if ch.isalnum():
            clean += ch
    return "Да" if clean == clean[::-1] else "Нет"

s = input()
print(is_palindrome(s))