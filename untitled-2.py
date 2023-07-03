from collections import Counter

def count_occurrences(lst):
    counter = Counter(lst)
    return counter
my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
occurrences = count_occurrences(my_list)
print(occurrences)