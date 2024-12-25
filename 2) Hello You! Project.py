# HELLO YOU PROJECT

# Ask user for their name

name = input("What is your name?:").strip().capitalize()

# Ask user for their age.

age = input("how old are you:").strip()

# Ask user about the city they live

city = input("What city do you live in?:").strip().capitalize()

#Ask user what they enjoy.

likes = input ("What are your hobbies?:")

# create output text

output = "Hello my name is {}. I am {} years old. I live in {}. I like {} .".format(name,age,city,likes)

# print output

print(output)
