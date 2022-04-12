from user import User
import re
import json
from dataclasses import asdict


def add_calories(calories, email):
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found')
    f.close()

    for i in range(len(temp)):
        if email in temp[i]:
            user = json.loads(temp[i])
            user['calories'].append(calories)
            temp[i] = json.dumps(user)
            temp[i] += '\n'
    try:
        with open('data.txt', 'w', encoding='utf-8') as file:
            file.writelines(temp)
    except FileNotFoundError:
        print('could not add data try again')
    print('Data saved successfully')
    f.close()


def plot_graph(email):
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found')
    f.close()
    data = None
    for i in range(len(temp)):
        if email in temp[i]:
            user = json.loads(temp[i])
            if user['calories']:
                data = user['calories']
                break
            else:
                print('No data to plot')
                return
    # y = data
    # x = list(range(1, len(data)+1))
    # plt.xlabel('days')
    # plt.ylabel('calories consumed')
    # plt.plot(x, y)
    # plt.show()


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = email.strip()
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


def store_new_user(data):
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

    while True:
        email = input('enter your email ')
        if validate_email(email):
            break
        else:
            print('please enter valid email!')

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
        print('email already taken! use new email')
        return

    user = User(name, email, height, weight, age, gender)
    bmi = bmi_calculator(height, weight)
    data = asdict(user)
    data['bmi'] = bmi
    data['calories'] = []
    data = json.dumps(data)
    store_new_user(data)


def add_data():
    while True:
        email = input('enter your email ')
        if validate_email(email):
            break
        else:
            print('please enter valid email address')
            continue

    if not exist(email):
        print('User not found, please signup')
        return

    while True:
        try:
            morning = float(input('enter the amount of calories consumed in morning '))
            afternoon = float(input('enter the amount of calories consumed in afternoon '))
            night = float(input('enter the amount of calories consumed in night '))
        except ValueError:
            print('Calories should be in number')
            continue
        else:
            break

    total_calories = morning + afternoon + night
    add_calories(total_calories, email)
    return


def display_data():
    while True:
        email = input('enter your email ')
        if validate_email(email):
            break
        else:
            print('please enter valid email address')
            continue

    if not exist(email):
        print('user does not exist please signup')
        return

    plot_graph(email)
