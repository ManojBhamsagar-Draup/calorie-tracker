from app_functions import add_data
from app_functions import display_data
from app_functions import signup


while True:
    print('1 signup\t 2 add data\t 3 display\t 4 quit')

    try:
        choice = int(input())
    except TypeError:
        print('looks like you did not enter an integer')
        continue
    else:
        if choice == 1:
            signup()
        elif choice == 2:
            add_data()
        elif choice == 3:
            display_data()
        elif choice == 4:
            break
print('Bye!')