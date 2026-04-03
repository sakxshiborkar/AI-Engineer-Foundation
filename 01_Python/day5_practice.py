# 1. f-string practice
name = input("What's your name? ").strip().title()
age = int(input("What's your age? "))
print(f"hello, {name}! You are {age} years old.")

# 2. sep and end
print("Python","is","amazing", sep="🔥")
print("Keep ", end="")
print("going!")

# 3. String methods
city = "   mumbai   "
print(city.strip().title())