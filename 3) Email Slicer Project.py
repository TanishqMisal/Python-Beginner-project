# EMAIL SLICER PROJECT

#get user email address

email = input("What is you email address?"). strip()

# slice out user name

user = email[:email.index("@")]

# slice out domain

domain = email[email.index("@") + 1:]

# format message

output = "Your user name is {} and your domain name is {}.".format(user,domain)

# display output message
print(output)
