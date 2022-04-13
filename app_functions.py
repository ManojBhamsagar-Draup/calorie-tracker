import json
# import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass()
class AddCalories:
    calories: float
    email: str

    def add_calories(self):
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
