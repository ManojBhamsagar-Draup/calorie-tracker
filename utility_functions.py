import re


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # regular expression for email
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def exist(data, file_name):
    """checks if user exist in the database"""
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('file not found, please retry')
        return False

    temp = f.readlines()
    for i in temp:
        if data in i:
            f.close()
            return True
    f.close()
    return False
