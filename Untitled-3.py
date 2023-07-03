def has_unique_elements(tup):
    return len(tup) == len(set(tup))
my_tuple = (1, 2, 3, 4, 5)
print(has_unique_elements(my_tuple))
my_tuple = (1, 2, 3, 4, 4, 5)
print(has_unique_elements(my_tuple))
