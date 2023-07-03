def remove_duplicates(lst):
    return list(set(lst))
my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
unique_list = remove_duplicates(my_list)
print(unique_list)