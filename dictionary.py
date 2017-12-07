# Dictionaries are mutable which means that they can be changed.
# The first item is the key, the second item is the value.

myCat =  {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# Size is the key, fat is the value.

print(myCat['size']) # prints out 'fat'


print('My cat has ' + myCat['color'] + ' fur.') 
# calls the dictionary definition and inserts to the sentence

# Items in dictionaries are unordered

[1,2,3] == [3,2,1] # lists order matters, this returns boolean False


# If compared, these will return a boolean True statement

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
print(eggs == ham)
# It returns as true because even though they're in different order they have the same key value pairs.

# If you know the word, you can get the definition. If you know the key, you can get the value.

# You can check if a key exists with in or not in operater.

print('name' in eggs) # returns True, there is a name key defined in eggs.
print('color' in ham) # returns False, there is no color key defined in ham.

print(list(eggs.keys())) # this will name what keys are in the list

for k in eggs.keys():
    print(k)
# assigns the key values to "k" and prints

for v in eggs.values():
    print(v)
# assigns the values of the keys to "v" and prints

for k, v in eggs.items():

# add