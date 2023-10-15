# script to check whether the given key already exists in a dictionary.

d = {1:100 , 2:200 , 3:300 , 4:400 , 5:500}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key not presnt in the dictionary')

is_key_present(4)