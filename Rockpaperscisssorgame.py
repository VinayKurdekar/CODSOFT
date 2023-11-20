import random


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"

    if (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def display_choices(player_choice, computer_choice):
    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")


def display_score(player_score, computer_score):
    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")


def main():
    player_score = 0
    computer_score = 0

    while True:
        print("\n====== Rock, Paper, Scissors ======")
        print("Choose: rock, paper, or scissors")
        print("To quit, type 'exit'")

        player_choice = input("Your choice: ").lower()

        if player_choice == 'exit':
            print("Thanks for playing!")
            break

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        display_choices(player_choice, computer_choice)
        result = determine_winner(player_choice, computer_choice)
        print(f"Result: {result}")

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        display_score(player_score, computer_score)


if __name__ == "__main__":
    main()
