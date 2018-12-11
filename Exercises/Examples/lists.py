# A string list
['cat', 'boy', 'tree']

# A numerical list
[1,2,3]

# Assigning a list to a variable
spam = ['cat', 'boy', 'tree']

print(spam) # Prints out the list
print(spam[1]) # Prints out the list item assigned to '1', which is 'boy'.

evenCount = list(range(0, 100, 2))
print(evenCount) # prints 0 - 98 in steps of two (does not include 100)

# Describes what is assigned to each index, starting at zero.
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) +  ' in supplies is: ' + supplies[i])


# A list of objects can be assigned to a variable by assigning the index to the left of a var with a list.
# Instead of having to assign them one by one.
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)

dog = ['friendly', 'cute', 'hyper']
dog.append('insane') # Adds "insane" to the list
print(dog)
dog.insert(1, 'slobbery') # Adds an item to a specific point in the list
print(dog)
dog.remove('insane') # Removes "insane" from the list
print(dog)


numbers = [2, 1, 4, -7]
numbers.sort() # This method will automatically sort lists for you
print(numbers)

reverseNumbers = [2, 1, 4, -7]
reverseNumbers.sort(reverse = True) # Sorts the numbers in reverse order
print(reverseNumbers)

# Lists can only be sorted if they contain one data type. 
# It cannot contain strings and intergers. Only one.

# Python actually sorts in "ASCII-betical", meaning capital letters will come first.
asciiList = ['Alice', 'game', 'RPG', 'Atlus', 'battle', 'strength']
asciiList.sort()
print(asciiList)

# To combat this, you could use the lower case argument.
asciiList.sort(key=str.lower)
print(asciiList)

# # List of Methods:
# index() - returns the index of an item in the list
# append() - adds a value to the end of a list
# insert() - adds a value anywhere inside a list
# remove() - removes a value from a list
# sort() - sorts the items in a list
# sort(reverse = True) - sorts the items in a list in reverse order
# sort(key=str.lower) - avoids the list being sorted in ASCII-betical order