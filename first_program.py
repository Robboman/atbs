# First program
# This program says hello and asks for my name and age
print("Hello, world!")
print("What's your name?")
name = input("Name: ")
print(f"It is good to meet you, {name}")
print(f"The length of your name is {len(name)} characters!")
age = int(input("How old are you? "))
print(f"You are {str(age)} years old!")
print(f"Also, you will be {str(age + 1)} years old in a year!")