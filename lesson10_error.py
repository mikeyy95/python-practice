def safe_int(value):
    try:
        new = int(value)
        return new
    except ValueError:
        return None

print(safe_int("123"))
print(safe_int("abc"))

def get_list_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Index out of range"

print(get_list_item([1, 2, 3], 1))
print(get_list_item([1, 2, 3], 5))

class NegativeValueError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeValueError("Cannot compute square root of a negative number")
    return n ** 0.5

try:
    print(square_root(-4))
except NegativeValueError as e:
    print(e)

def risky():
    try:
        return 1 / 0
    except ZeroDivisionError:
        return "caught"
    finally:
        print("cleanup ran")

print(risky())