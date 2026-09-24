number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

for i in range(21):
    if (i%3==0):
        continue
    else:
        print(i)

while True:
    password = input("Enter Password: ")
    if password == "secret123":
        print("Access granted.")
        break
    else:
        print("Access denied. Try again.")