import random
correct_number = 1
guess = ()
guess_count = 1
while guess != correct_number:
    guess = (int(input('What\'s your guess?: ')))
    correct_number = random.randint(1,5)
    print('The correct number is:',correct_number)
    guess_count += 1
    if guess == correct_number:
        print(f'Congratulations, you chose the right number! The correnct number was {correct_number} you needed {guess_count} guesses to find it.')
        break
    else:
        if guess > correct_number:
            print('You guessed too high!')
        else:
            print('You guessed too low!')
    print('You chose the wrong, number, try again')
    