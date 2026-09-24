def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))

def max_of_three(a,b,c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum

print(max_of_three(3, 7, 5))
print(max_of_three(10, 2, 8))

def greet_func(name,greetings="Hi"):
    print(f"{greetings}, {name}!")

greet_func("Anvay")
greet_func("Anvay", "Welcome")