import json
# import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass()
class AddCalories:
    calories: float
    email: str

    def add_calories(self):
        """adding user's daily calorie consumption."""

        try:
            with open('data.txt', 'r', encoding='utf-8') as f:
                temp = f.readlines()
        except FileNotFoundError:
            print('file not found')
            return False

        f.close()

        for i in range(len(temp)):
            if self.email in temp[i]:
                user = json.loads(temp[i])
                user['calories'].append(self.calories)
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


@dataclass()
class PlotGraph:
    email: str

    def plot_graph(self):
        """Plotting user's data on graph."""

        try:
            with open('data.txt', 'r', encoding='utf-8') as f:
                temp = f.readlines()
        except FileNotFoundError:
            print('file not found')
            return

        f.close()
        data = None
        for i in range(len(temp)):
            if self.email in temp[i]:
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
        # plt.title('self.email')
        # plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,marker='o',
        #               markerfacecolor='blue', markersize=12)
        # plt.show()


def display_user_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found')
        return

    f.close()
    print("{}\t {}\t\t\t\t {}\t".format('Name', 'Email', 'BMI'))
    for i in range(len(temp)):
        data = json.loads(temp[i])
        print("{}\t {}\t {}\t".format(data['name'], data['email'], data['bmi']))


def delete_user(data, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found')
        return False
    f.close()

    for i in temp:
        if data in i:
            temp.remove(i)
            break

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines(temp)
    except FileNotFoundError:
        print('something went wrong')
        return False

    f.close()
    return True


def set_new_password(new_password, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found')
        return False
    f.close()

    temp[1] = new_password

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines(temp)
    except FileNotFoundError:
        print('something went wrong')
        return False

    f.close()
    return True
