import random


def play():
    user = input("'r' for rock\n'p' for paper\n's' for scissor:\n ")
    computer = random.choice(["r", "p", "s"])
    return user, computer


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    else:
        if user == "r":
            if computer == "p":
                return "lose"
            else:
                return "win"
        elif user == "p":
            if computer == "s":
                return "lose"
            else:
                return "win"
        else:
            if computer == "r":
                return "lose"
            else:
                return "win"


if __name__ == '__main__':
    user, computer = play()
    result = determine_winner(user, computer)
    if result == "tie":
        print("It's a draw!!")
    elif result == "lose":
        print("Computer has won!")
    else:
        print("You win!")