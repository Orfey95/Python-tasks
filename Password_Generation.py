import re
import random


def password_generation():
    print("Input password pattern (example: 2a11A4d7S):")
    pattern = input()
    if pattern == '':
        pattern = '2a11A4d7S'
    password = ''  # password variable declaration
    # verify password pattern
    if not re.match(r'^(\d+[aAdS]+)+$', pattern):
        return print("Errors in the password pattern, correct them. Here is an example: 2a11A4d7S")
    # get from the password pattern, the part that is responsible for lowercase letters
    lowercase_letters_pattern = re.search(r'\d*a', pattern)
    # get from the password pattern, the part that is responsible for uppercase letters
    uppercase_letters_pattern = re.search(r'\d*A', pattern)
    # get from the password pattern, the part that is responsible for digits
    digits_pattern = re.search(r'\d*d', pattern)
    # get from the password pattern, the part that is responsible for special symbols
    special_symbols_pattern = re.search(r'\d*S', pattern)
    if bool(lowercase_letters_pattern):
        number_of_lowercase_letters = str(lowercase_letters_pattern[0])[:-1]  # get number of lowercase letters
        for x in range(int(number_of_lowercase_letters)):
            password += chr(random.randint(97, 122))  # generate and add lowercase letters to password
    if bool(uppercase_letters_pattern):
        number_of_uppercase_letters = str(uppercase_letters_pattern[0])[:-1]  # get number of uppercase letters
        for x in range(int(number_of_uppercase_letters)):
            password += chr(random.randint(65, 90))  # generate and add uppercase letters to password
    if bool(digits_pattern):
        number_of_digits = str(digits_pattern[0])[:-1]  # get number of digits
        for x in range(int(number_of_digits)):
            password += chr(random.randint(48, 57))  # generate and add digits to password
    if bool(special_symbols_pattern):
        number_of_special_symbols = str(special_symbols_pattern[0])[:-1]  # get number of special symbols
        list_of_special_symbols = ("+", "-", "*", "/", "#", "$", "%", "^", ":", ";", "~", "&", "?", "|")
        for x in range(int(number_of_special_symbols)):
            password += random.choice(list_of_special_symbols)  # generate and add special symbols to password
    # shuffle characters in a password
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return "Your password: " + password


print(password_generation())
