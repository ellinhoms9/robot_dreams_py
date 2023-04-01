first_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
second_set = {6, 7, 8, 9, 10, 11, 12, 13}


def intersection_of_two_sets(first, second):
    return first.intersection(second)


def symmetric_difference_of_two_sets(first, second):
    return first.symmetric_difference(second)


print(intersection_of_two_sets(first_set, second_set))
print(symmetric_difference_of_two_sets(first_set, second_set))
