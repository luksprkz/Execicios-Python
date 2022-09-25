choice = ''
user_text = input('What do you wanna say? ')
while choice != ('a','b'):
    choice = input('Enter: \na.upper case  \nb. lower case ')
    if choice == 'a':
        print(user_text.upper())
        break
    elif choice == 'b':
        print(user_text.lower())
        break
    print('Thats not a valid choice, try again')
    

