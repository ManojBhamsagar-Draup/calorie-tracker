from app_functions import signup, add_calories, plot_graph
from utility_functions import exist, validate_email
import re


while True:
    print('1 signup\t 2 add data\t 3 display\t 4 quit')

    try:
        choice = int(input())
    except TypeError:
        print('looks like you did not enter an integer')
        continue
    except ValueError:
        print('Invalid key entered')
    else:
        if choice == 1:
            while True:
                name = input('enter your name ')
                name = name.strip()
                if re.match(r'[a-zA-Z]+$', name):
                    break
                else:
                    print('name should only contain letters and spaces')

            while True:
                email = input('enter your email ')
                email = email.strip()
                if validate_email(email):
                    if exist(email):
                        print('email already taken please try with another email')
                        continue
                    else:
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
                except (TypeError, ValueError):
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

            signup(name, email, height, weight, gender, age)

        elif choice == 2:
            while True:
                email = input('enter your email ')
                email = email.strip()
                if validate_email(email):
                    break
                else:
                    print('please enter valid email address')
                    continue
            if not exist(email):
                print('User not found, please signup')
            else:
                while True:
                    try:
                        morning = float(input('enter the amount of calories consumed in morning '))
                        afternoon = float(input('enter the amount of calories consumed in afternoon '))
                        night = float(input('enter the amount of calories consumed in night '))
                        extra = float(input('extra calories consumed '))
                    except ValueError:
                        print('Calories should be in number')
                        continue
                    else:
                        break

                total_calories = morning + afternoon + night + extra
                add_calories(total_calories, email)

        elif choice == 3:
            while True:
                email = input('enter your email ')
                email = email.strip()
                if validate_email(email):
                    break
                else:
                    print('please enter valid email address')
                    continue
            if not exist(email):
                print('user does not exist please signup')
            else:
                plot_graph(email)

        elif choice == 4:
            break
        else:
            print('invalid choice!')
print('Bye!')
