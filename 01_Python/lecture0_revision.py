# 1. Ask user for their name and greet them with f-string
name = input("What's your name?").strip().title()
print(f"Hello, {name}!")

# 2. Ask for their age, calculate days alive
age = int(input("What's your age?"))
days = age * 365
print(f"You have been alive for {days} days.")

# 3. Create a list of 3 goals, print first and last
goals = ["Python" , "AI" , "SpaceX" ]
print("First goal:" , goals[0])
print("Last goal:" , goals[-1])

# 4. Write a function called greet() that takes a name and prints hello
def greet(name):
    print("Hello, ", name)

greet("Sakshi")