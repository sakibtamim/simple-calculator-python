while True:
    choice = input(f"What do you want: \n 1. addition\n 2. subtraction"
                   f"\n 3. multiplication\n 4. division\n : ")

    if choice in ('1', '2', '3', '4'):
        try:
            x = float(input("X: "))
            y = float(input("Y: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            add = x + y
            print("addition = " + str(add))
        elif choice == '2':
            subs = x - y
            print("subtraction = " + str(subs))
        elif choice == '3':
            multi = x * y
            print("multiplication = " + str(multi))
        elif choice == '4':
            div = x / y
            print("division = " + str(div))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print("Thank You!")
            break
    else:
        print("Sorry! You should enter a choice.")
