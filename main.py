from utility_functions import exist, validate_email
from app_functions import AddCalories, PlotGraph, display_user_data, delete_user, set_new_password
from user import User
import re


while True:
    print('1 signup\t 2 add data\t 3 display\t 4 admin login\t 5 quit')

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
                    if exist(email, 'data.txt'):
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
            user = User(name, email, height, weight, age, gender, 0.0, [])
            success = user.signup(user)
            if success:
                print('Hi {}, signed up successfully'.format(user.name))
                user.bmi_outputter()
            else:
                print('File not found, please retry signing up')

        elif choice == 2:
            while True:
                email = input('enter your email ')
                email = email.strip()
                if validate_email(email):
                    break
                else:
                    print('please enter valid email address')
                    continue
            if not exist(email, 'data.txt'):
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
                add = AddCalories(total_calories, email)
                add.add_calories()

        elif choice == 3:
            while True:
                email = input('enter your email ')
                email = email.strip()
                if validate_email(email):
                    break
                else:
                    print('please enter valid email address')
                    continue
            if not exist(email, 'data.txt'):
                print('user does not exist please signup')
            else:
                graph = PlotGraph(email)
                graph.plot_graph()

        elif choice == 4:
            while True:
                email = input('enter your email ')
                email = email.strip()
                if validate_email(email):
                    break
                else:
                    print('enter valid email address')
                    continue
            if not exist(email, 'admin.txt'):
                print('email address is wrong')
                continue
            else:
                while True:
                    password = input('enter password ').strip()
                    if not exist(password, 'admin.txt'):
                        print("password doesn't match")
                        continue
                    else:
                        while True:
                            print("1 check user's data\t 2 delete user\t 3 change password\t 4 logout")
                            try:
                                admin_choice = int(input())
                            except TypeError:
                                print('looks like you did not enter an integer')
                                continue
                            except ValueError:
                                print('Invalid key entered')
                            else:
                                if admin_choice == 1:
                                    display_user_data('data.txt')
                                elif admin_choice == 2:
                                    while True:
                                        email = input('enter email of the user you want to delete ').strip()
                                        if not validate_email(email):
                                            print('enter valid email address')
                                        else:
                                            break
                                    if exist(email, 'data.txt'):
                                        if delete_user(email, 'data.txt'):
                                            print('user deleted successfully')
                                        else:
                                            print('unable to delete user data')
                                    else:
                                        print("user with the given email doesn't exists")

                                elif admin_choice == 3:
                                    new_password = input('enter new password ').strip()
                                    if set_new_password(new_password, 'admin.txt'):
                                        print("password set successfully")
                                    else:
                                        print("unable to set new password, try again")
                                elif admin_choice == 4:
                                    break
                                else:
                                    print('invalid choice')
                        break

        elif choice == 5:
            break

        else:
            print('invalid choice!')
print('Bye!')
