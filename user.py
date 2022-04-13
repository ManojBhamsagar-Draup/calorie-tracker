from dataclasses import dataclass, asdict
import json


@dataclass
class User:
    name: str
    email: str
    height: float
    weight: float
    age: int
    gender: str
    bmi: float
    calories: list

    def __post_init__(self):
        self.bmi = round((self.weight / (self.height ** 2)), 2)
        self.calories = []

    def signup(self, user):
        data = asdict(user)
        data = json.dumps(data)

        try:
            f = open('data.txt', 'a')
        except FileNotFoundError:
            return False

        f.write(data + '\n')
        f.close()
        return True

    def bmi_outputter(self):
        if self.bmi <= 18.5:
            print("Your physical health status is underweight, try to consume more calories and maintain good diet.")
        elif 18.5 < self.bmi <= 24.9:
            print("Your physical health status is normal and Healthy weight, Good going!")
        elif 25.0 < self.bmi <= 29.9:
            print("Your physical health status is overweight, try to do daily exercise and maintain good diet.")
        else:
            print("Your physical health status is Obese, consume less calories and avoid junk food")





