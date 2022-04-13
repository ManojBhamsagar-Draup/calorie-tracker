import re


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def exist(email):
    try:
        f = open('data.txt', 'r')
    except FileNotFoundError:
        print('file not found, please retry')
        return

    temp = f.readlines()
    for i in temp:
        if email in i:
            f.close()
            return True
    f.close()
    return False
