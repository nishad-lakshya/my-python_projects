current_year = 2025
Name = input("Enter your name:")
Age = int(input("enter yout birth year:"))
current_age = current_year - Age 
print(current_age)
if current_age > 18:
    print("your a adult")
else:
    print("you are minor")
