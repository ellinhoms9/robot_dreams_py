print(""" Telephone book
1. Stats (if you want to view the number of records, enter "1")
2. Add (if you want to add a record, enter "2")
3. Delete (if you want to delete the record, enter "3")
4. List (if you want to see a list of all names in the book, enter "4")
5. Show (if you want to view detailed information by name, enter "5")
6. Exit (if you want to end the program, enter "6")
      """)


telephone_book = {}
while True:
    choise = int(input("Please enter your choice: "))
    if choise == 1:
        def stats():
            print(len(telephone_book))
    elif choise == 2:
        def adds():
            name = input("Please enter name and last name: ")
            telephone = input("Please enter telephone number: ")
            # checking whether the entered data is correct and whether this name is not in the phone book
            if len(name) < 4 or len(telephone) < 9:
                print("Incorrect name or phone number, please check and try again.")
            elif name in telephone_book:
                print("This contact is already in the phone book.")
            else:
                telephone_book[name] = telephone
    elif choise == 3:
        def delete():
            del_number = input("Please enter the name whose record you want to delete: ")
            del telephone_book[del_number]
    elif choise == 4:
        def book_keys():
            print(telephone_book.keys())
    elif choise == 5:
        def search_in_book():
            search_name = input("Please enter the name whose record you are looking for: ")
            # checking whether this contact is in the phone book.
            if search_name in telephone_book:
                print(search_name, "-", telephone_book.get(search_name))
            else:
                print("This name is not in the phone book, please check and try again.")
    elif choise == 6:
        break
    else:
        print("Incorrect input")
