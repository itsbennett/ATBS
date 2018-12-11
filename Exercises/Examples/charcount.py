# A program that counts the number of occurances of a letter in a string.

import pprint # stands for pretty print, prints lists nicely

word = "Supercalifragilisticexpialidocious"
count = {} # creates a dictionary for "count"

for character in word.upper(): 
    # the upper method allows all instances of a letter to be counted instead of seperated by upper and lower case.
    count.setdefault(character, 0) 
    # sets the value of each character to zero by default
    count[character] = count[character] + 1 
    # increments the count by one each time it's encountered

pprint.pprint(count)