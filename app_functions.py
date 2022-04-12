from user import User
import re
import json
from dataclasses import asdict


def exist(email):
    try:
        f = open('data.txt', 'r')
    except FileNotFoundError:
        print('file not found, please retry')
        return

    temp = f.readlines()
    for i in temp:
        if email in i:
            print('email already taken please use new email')
            return True
    return False


def store_new_user(data, email):
    try:
        f = open('data.txt', 'a')
    except FileNotFoundError:
        print('File not found, please retry signing up')
        return

    f.write(data + '\n')
    f.close()
    print("Signed up successfully!")


def bmi_calculator(height, weight):
    bmi = round((weight / (height ** 2)), 2)
    print('your BMI is {}'.format(bmi))

    if bmi <= 18.5:
        print("Your physical health status is underweight, try to consume more calories and maintain good diet.")
    elif 18.5 < bmi <= 24.9:
        print("Your physical health status is normal and Healthy weight, Good going!")
    elif 25.0 < bmi <= 29.9:
        print("Your physical health status is overweight, try to do daily exercise and maintain good diet.")
    else:
        print("Your physical health status is Obese, consume less calories and avoid junk food")

    return bmi


def signup():
    while True:
        name = input('enter your name ')
        name = name.strip()
        if re.match(r'[a-zA-Z]+$', name):
            break
        else:
            print('name should only contain letters and spaces')
            continue

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        email = input('enter your email ')
        email = email.strip()
        if re.fullmatch(regex, email):
            break
        else:
            print('please enter valid email address')

    while True:
        try:
            print('enter height in meters and weight in kgs ')
            height, weight = [float(i) for i in input().split()]
        except ValueError:
            print('please enter height and weight in numbers with a space between them')
            continue
        else:
            break

    while True:
        try:
            print('enter your age ')
            age = int(input())
        except TypeError:
            print('age should be number')
            continue
        else:
            break

    while True:
        print("please mention your gender 'm' male\t 'f' female\t 'o' others ")
        gender = input()
        if gender in 'mMfFoO':
            break
        else:
            print('please enter only mentioned characters')
            continue

    if exist(email):
        return

    user = User(name, email, height, weight, age, gender)
    bmi = bmi_calculator(height, weight)
    data = asdict(user)
    data['bmi'] = bmi
    data['calories'] = []
    data = json.dumps(data)
    store_new_user(data, email)


def add_data():
    pass


def display_data():
    pass