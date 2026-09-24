student = {"name": "Anvay", "marks": [85, 90, 78]}
print(sum(student["marks"]) / len(student["marks"]))

def count_words(string):
    word_count ={}
    words = string.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_words("the cat sat on the mat"))

inventory = {"apples": 10, "bananas": 5, "mangoes": 0}
for i in inventory:
    if inventory[i] > 0:
        print(i)