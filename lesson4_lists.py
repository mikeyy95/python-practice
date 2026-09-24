nums = [10,20,30,40,50]
print(nums[:2])
print(nums[-2:])
print(nums[::-1])

data = [5, 3, 8, 1, 9, 2]
print(sorted(data))
print(data)

def remove_duplicates(lst):
    print(lst)
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

print(remove_duplicates([5, 4, 4, 3, 2, 2, 1, 1]))