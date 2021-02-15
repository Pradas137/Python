def menu_generator(*options, header="\n"):
    flag_menu = False
    while not flag_menu:
        print(header)
        for i in range(len(options)):
            print(i+1, ")", options[i])
        try:
            user_option = int(input("Choose an option: "))
            if 0 < user_option <= len(options):
                flag_menu = True
                return user_option
            else:
                print("Invalid option.")
                flag_menu = False
        except ValueError:
            print("That's no a number. Try again.")

print(menu_generator("List by ID", "List by name", "List by Stock", "Back", header='MAIN MENU'))
