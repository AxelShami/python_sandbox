# A List is a collection which is ordered and changeable. Allows duplicate members.


# Use a constructor
# numbers2 = list((1,2,3,4,5))


# Creat list 
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges','Grapes','Pears']

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into a position
fruits.insert(2,'strawberries')

# Change value
fruits[0] = 'Blueberries'
# Remove with pos
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)