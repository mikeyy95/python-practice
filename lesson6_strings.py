def clean_and_split(sentence):
    s = sentence.split(",")
    s = [item.strip() for item in s]
    return s
print(clean_and_split("  Hello,   World  ,Python  "))

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))

words = ["apple", "fig", "banana", "kiwi"]
letter_count = {i : len(i) for i in words}
print(letter_count)