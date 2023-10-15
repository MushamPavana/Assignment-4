##Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
#Sample string : 'marolix technology'
#Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}


string = "marolix technology"
dictionary = {}
for i in string:
    if i in dictionary:
        continue
    elif i==" ":
        continue
    else:
        dictionary[i]=string.count(i)
        print(dictionary)