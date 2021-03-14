"""
# Write a method "combination" that takes in a list of 
# unique elements, and returns a 2D list representing 
# all possible combinations of 2 elements of the list.
"""


def combinations_2(my_list): 
    final_list = []
    for i in range(len(my_list)):
        j = i + 1
        for j in range(j, len(my_list)):
            temp_list = []
            temp_list.append(my_list[i])
            temp_list.append(my_list[j])
            final_list.append(temp_list)
    return final_list
 
print(combinations_2(['a', 'b', 'c', 'd','e', 'f']))