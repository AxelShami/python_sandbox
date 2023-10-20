# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Axel'
age = 20

#Concatenate (meaning insert a variable into a str)
#print('Hello, my name is ' + name + ' and I am '+ str(age))

# String Formatting

#Arguments by position
# print('My name is {name} and I am {age}'.format(name = name, age = age)) # The format method act like a place horder, so wathever is in () will show up

#F-Strings (available : 3.6+ version)
# print(f'Hello, my name is {name} and I am {age}') 


# String Methods

s ='helloword'

# Capitaliza string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello')) # return True or False

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split()) # Take the str and trun it into a list

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
