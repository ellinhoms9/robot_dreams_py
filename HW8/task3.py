def string_elem_to_up(elem):
    print(f'Argument of function: {elem}')
    if type(elem) == str:
        return elem.upper()
    else:
        return "This element is not type string."


lst = [1, "a", 2.1, "B", 3, "c", 4.7, "d", 5]
# mapping
for item in map(string_elem_to_up, lst):
    print(item)
