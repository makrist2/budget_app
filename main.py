import db_operations
import datetime

while True:
    print('-~-~-~-~-~-MAIN MENU-~-~-~-~-~-~-~')
    menu = input("""Enter number:
    1. Add value
    2. Delete something
    3. Show values
    4. Show budgets
    5. Exit
    """)

    if menu == '1':  # add
        print('-~-~-~-~-~-ADDING MENU-~-~-~-~-~-~-~')
        cat = input('Choose category: 1 - Food, 2 - Other\n')
        try:
            if cat == '1':
                money = int(input('Enter price of the food: '))
                food_name = input('Enter food name: ')
                db_operations.insert_food(food_name, money, datetime.date.today())
                print(f'Successfully added {food_name} to the list!')
            if cat == '2':
                money = int(input('Enter price of the item: '))
                other_name = input('Enter its name: ')
                db_operations.insert_other(other_name, money, datetime.date.today())
                print(f'Successfully added {other_name} to the list!')
        except Exception as e:
            print('Something went wrong. Oops!')

    elif menu == '2':  # delete
        print('-~-~-~-~-~-DELETING MENU-~-~-~-~-~-~-~')
        cat = input('Choose category to delete: 1 - Food, 2 - Other, 3 - Clear all data\n')
        try:
            if cat == '1':
                db_operations.delete_food()
                print('Deleted everything from <Food> category!\n')
            if cat == '2':
                db_operations.delete_other()
                print('Deleted everything from <Other> category!\n')
            if cat == '3':
                db_operations.delete_everything()
                print('Everything is gone... Are you happy now?\n')
        except Exception as e:
            print('Something went wrong. Oops!')

    elif menu == '3':  # show
        print('-~-~-~-~-~-INFO MENU-~-~-~-~-~-~-~')
        cat = input('Choose category: 1 - Food, 2 - Other, 3 - All\n')
        try:
            if cat == '1':
                print('------- Food category info: -------\n')
                print(db_operations.select_all_food())
                print('-------------------------')
            if cat == '2':
                print('------- Other category info: -------\n')
                print(db_operations.select_all_other())
                print('-------------------------')
            if cat == '3':
                print('------- Food category info: -------\n')
                print(db_operations.select_all_food())
                print('------- Other category info: -------\n')
                print(db_operations.select_all_other())
                print('-------------------------')
        except Exception as e:
            print('Something went wrong. Oops!')

    elif menu == '4':  # show summ price for category
        print('-~-~-~-~-~-GENERAL PRICE MENU-~-~-~-~-~-~-~')
        cat = input('Choose category: 1 - Food, 2 - Other, 3 - All\n')
        try:
            if cat == '1':
                print('------- Food category sum info: -------\n')
                print(f'Food price summary: {db_operations.select_food_price_sum()}')
                print('-------------------------')
            if cat == '2':
                print('------- Other category info: -------\n')
                print(f'Other price summary: {db_operations.select_other_price_sum()}')
                print('-------------------------')
            if cat == '3':
                print('------- All categories info: -------\n')
                res = db_operations.select_food_price_sum() + db_operations.select_other_price_sum()
                print(f'Total sum: {res}')
                print('-------------------------')
        except Exception as e:
            print('Something went wrong. Oops!')

    elif menu == '5':  # exit
        print('Bye, have a beautiful time!')
        break

    else:
        print(f'Yeah, {menu} is {menu}')
