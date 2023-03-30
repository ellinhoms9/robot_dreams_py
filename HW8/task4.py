def filter_int(elem):
    # check type of elements
    if type(elem) == int or type(elem) == float:
        return elem


data = [1, "a", 2.1, "B", 3, "c", 4.7, "d", 5]
# filtering
for item in filter(filter_int, data):
    print(item)