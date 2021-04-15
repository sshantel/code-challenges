""" 
Playing with dictionary methods
""" 
def dict_methods(dict):

#clear() - Removes all elements from dictionary
    dict.clear()
# copy()	Returns a copy of the dictionary
    dict.copy()
# fromkeys()	Returns a dictionary with the specified keys and value
    x = ('cheese', 'bread', 'cake')
    y = 0
    new_dict = dict.fromkeys(x, y)
    print(new_dict)
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the 


dict_methods({1:2,3:4,5:6})
dict_methods({'dog':5, 'cat':1, 'monkey': 2, 'baboon': 6})

