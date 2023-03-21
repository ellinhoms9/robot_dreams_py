users_text = input("Please input some text: ")
# check if an empty string is entered
if len(users_text) == 0:
    print("You have not entered anything.")
else:
    for elem in users_text:
        # check if the element from input text is a number
        if elem.isdigit():
            if int(elem) == 0:
                print(f"elem: {elem} - This is number. This number is not even and not odd.")
            elif int(elem) % 2 == 0:
                print(f"elem: {elem} - This is number. This number is even.")
            else:
                print(f"elem: {elem} - This is number. This number is odd.")
        # check if the element from input text is a word
        elif elem.isalpha():
            if elem.islower():
                print(f"elem: {elem} - This is a small letter.")
            else:
                print(f"elem: {elem} - This is a capital letter.")
        else:
            print(f"elem: {elem} - This is a symbol.")
