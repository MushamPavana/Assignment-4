##Write a Python script to merge two Python dictionaries.d

dict1 = {"pavana":90,"yashu":87,"shraddha":90}
dict2 = {"naresh": 78,"shraddha":95,"triveni":85}

dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)