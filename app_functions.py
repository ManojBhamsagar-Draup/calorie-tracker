from user import User
import json
from dataclasses import asdict


def add_calories(calories, email):
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found')
        return

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
        return

    print('Data saved successfully')
    f.close()


def plot_graph(email):
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found')
        return

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


def signup(name, email, height, weight, age, gender):
    user = User(name, email, height, weight, age, gender)
    data = asdict(user)
    data['calories'] = []
    data = json.dumps(data)

    try:
        f = open('data.txt', 'a')
    except FileNotFoundError:
        print('File not found, please retry signing up')
        return

    f.write(data + '\n')
    f.close()

    print('Hi {}, signed up successfully'.format(user.name))
    if user.bmi <= 18.5:
        print("Your physical health status is underweight, try to consume more calories and maintain good diet.")
    elif 18.5 < user.bmi <= 24.9:
        print("Your physical health status is normal and Healthy weight, Good going!")
    elif 25.0 < user.bmi <= 29.9:
        print("Your physical health status is overweight, try to do daily exercise and maintain good diet.")
    else:
        print("Your physical health status is Obese, consume less calories and avoid junk food")
