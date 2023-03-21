def max_elem_with_build_in(*args):
    return max(args)


def max_elem_with_own_func(*args):
    max_number = 0
    for elem in args:
        if elem > max_number:
            max_number = elem
    return max_number


max_lamb = lambda *args: max(args)    # or max_lamb = lambda *args: max_elem_with_own_func(*args)


print(max_elem_with_build_in(1, 4, 5, 78, 4535,  -100))
print(max_elem_with_own_func(1, 4, 5, 78, 4535,  -100))
print(max_lamb(1, 4, 5, 78, 4535,  -100))
