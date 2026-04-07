# Problem 1: Echo Chamber: Take a user input and print it in lowercase.
name = input("What are you so excited about? ")
print((name).lower())

# Problem 2: Indoor Voice (CS50 classic): Same idea, but force yourself to write it cleanly in 1 line
name = print(input("What are you excited about? ").lower())

# Problem 3: Playback Speed: Replace all spaces " " with "..."

text = input("Enter text: ")
print(text.replace(" ", "..."))

# Problem 4: Even or Odd

x = int(input("Enter number: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Problem 5: Grade System

marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")

# Problem 6: Simple Calculator

def calculator(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter operation: ")

print(calculator(x, y, operation))