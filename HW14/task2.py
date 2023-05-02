import re

file_name = input("Please please enter a file name: ")
# open the file for reading and editing
with open(file_name, "r+") as file:
    txt = file.read()
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    # changing the data
    text_with_changes = re.sub(email_pattern, "@", txt)
    file.seek(0)
    # overwrite the file
    file.write(text_with_changes)
    file.truncate()
    print("File is changed.")
