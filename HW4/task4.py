# definition of the data type of the entered text
users_text = input("Please input the text: ")
# checking the data type and outputting the result
match users_text:
    case "":
        print("You have entered an empty string")
    case str() if users_text.isdigit():
        print("You entered an integer")
    case str() if users_text.isalpha():
        print("You have entered a string")
    case _:
        print("You entered a different data type")
