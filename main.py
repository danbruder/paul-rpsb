import random
import numbers


def choices(): 
    return ['rock', 'paper', 'boat', 'scissors']

def get_computer_choice(index):
    pattern = [1, 2, 4, 3, 3, 4, 2, 1]
    return choices()[pattern[index] - 1]

def get_user_choice():
    choice = input("Choose rock (1), paper (2), boat (3), or scissors (4): ").lower()
    try: 
        choice_number = int(choice)
        if choice_number > 0 and choice_number <= 4:
            return choices()[choice_number - 1]
        else: 
            while choice not in choices():
                choice = input("Invalid choice. Please choose rock, paper, boat, or scissors: ").lower()
            return choice
    except ValueError:
        while choice not in choices():
            choice = input("Invalid choice. Please choose rock, paper, boat, or scissors: ").lower()
        return choice

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It's a tie!"
    elif (computer_choice == 'rock' and user_choice == 'boat') or \
         (computer_choice == 'boat' and user_choice == 'rock'): 
        return "It's a boat tie"
    elif (computer_choice == 'rock' and user_choice == 'scissors') or \
         (computer_choice == 'scissors' and user_choice == 'paper') or \
         (computer_choice == 'boat' and user_choice == 'paper') or \
         (computer_choice == 'scissors' and user_choice == 'boat') or \
         (computer_choice == 'paper' and user_choice == 'rock'):
        return "Computer wins!"
    else:
        return "You win!"

def play():
    choice_index = 0
    while True:
        computer_choice = get_computer_choice(choice_index)
        user_choice = get_user_choice()
        print(f"Computer chose {computer_choice}.")
        print(f"User chose {user_choice}.")
        print(determine_winner(computer_choice, user_choice))
        
        choice_index += 1
        if choice_index == 8:
            choice_index = 0
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play()

