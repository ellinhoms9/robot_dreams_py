import json
import re


def stats():
    print(len(telephone_book))


def adds():
    name = input("Please enter name and last name: ")
    # checking whether the entered data is correct and whether this name is not in the phone book
    if len(name) < 3:
        print("Incorrect name, please check and try again.")
    elif name in telephone_book:
        print("This contact is already in the phone book.")
    else:
        telephone = input("Please enter telephone number: ")
        # create a pattern of phone number validation
        phone_number_validation = r"^(\+380|380|0)\d{9}$"
        # checking the entered number for validity
        if re.search(phone_number_validation, telephone):
            telephone_book[name] = telephone
            print("The contact has been successfully added to the phone book.")
            # update the json file
            updating_json_file()
        else:
            print("Incorrect telephone number, please check. "
                  "You must enter a Ukrainian number in format (+380xxxxxxxx, 380xxxxxxxxx, 0xxxxxxxxx)")


def delete():
    del_number = input("Please enter the name whose record you want to delete: ")
    try:
        del telephone_book[del_number]
        print(f"The record for {del_number} has been successfully deleted.")
        # update the json file
        updating_json_file()
    except KeyError:
        print(f"Key {del_number} does not exist in the telephone book.")


def book_keys():
    print(telephone_book.keys())


def search_in_book():
    search_name = input("Please enter the name whose record you are looking for: ")
    try:
        print(search_name, "-", telephone_book[search_name])
    except KeyError:
        print(f"Key {search_name} does not exist in the telephone book.")


def updating_json_file():
    json_telephone_book = json.dumps(telephone_book)
    with open("json_telephone_book.json", "w") as file:
        file.write(json_telephone_book)


print(""" Telephone book
1. Stats (if you want to view the number of records, enter "1")
2. Add (if you want to add a record, enter "2")
3. Delete (if you want to delete the record, enter "3")
4. List (if you want to see a list of all names in the book, enter "4")
5. Show (if you want to view detailed information by name, enter "5")
6. Exit (if you want to end the program, enter "6")
      """)


try:
    telephone_book = {}
    json_telephone_book = json.dumps(telephone_book)
    with open("json_telephone_book.json", "x") as file:
        file.write(json_telephone_book)
except FileExistsError:
    with open("json_telephone_book.json", "r") as file:
        the_contents_of_the_book = file.read()
        telephone_book = json.loads(the_contents_of_the_book)


while True:
    try:
        choise = int(input("Please enter your choice: "))
    except ValueError:
        print(f"Please enter an integer and see the instructions given at the beginning of the program.")
    if choise == 1:
        stats()
    elif choise == 2:
        adds()
    elif choise == 3:
        delete()
    elif choise == 4:
        book_keys()
    elif choise == 5:
        search_in_book()
    elif choise == 6:
        break
    else:
        print("Incorrect input")
