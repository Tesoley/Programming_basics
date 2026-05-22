message1 = input("Enter your name: ")
message2 = input("Enter your age: ")
print(f"{message1} {message2}")

# another example:
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
birth_year = 2026 - age
print(f"Your name is {name} \nYour age is {age} \nYour birth year is {birth_year} \n")

total = 12
amount = 5
print(total // amount)
print(total % amount)