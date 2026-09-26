def is_vowels(char):
    return char.lower() in 'aeiou'

def count_vowels(char):
    return sum(1 for c in char if c.lower() in 'aeiou')