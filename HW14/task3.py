import re

file_name = input("Please please enter a file name: ")
# open the file for reading and editing
with open(file_name, "r+") as file:
    txt = file.read()
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    def change_mail(match):
        email = match.group(0)
        new_mail = (email[0] + "******@******" + email[-1])
        return new_mail


    # changing the data
    text_with_changes = re.sub(email_pattern, change_mail, txt)
    file.seek(0)
    # overwrite the file
    file.write(text_with_changes)
    file.truncate()
    print("File is changed.")
