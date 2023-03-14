users_text = input("Please input the text: ")
# check if the text is a number
if users_text.isdigit():
    print("This is a number.")
    if int(users_text) == 0:
        print("This number is not even and not odd.")
    elif int(users_text) % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")
# check if the text is a word
elif users_text.isalpha():
    print(f"This is a word. Length of this word is {len(users_text)}.")
else:
    print("It is not a word or a number.")







