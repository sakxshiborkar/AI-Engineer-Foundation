age = int(input("What's your age? "))

if age < 13:
    print("You are a child")

elif age < 18:
    print("You are a teenager")

elif age < 65:
    print("You are an adult")

else:
    print("You are a senior")