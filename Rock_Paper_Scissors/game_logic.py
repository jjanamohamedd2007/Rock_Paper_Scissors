
def get_choice(fingers):

    if fingers == [0, 0, 0, 0, 0]:
        return "Rock"

    elif fingers == [1, 1, 1, 1, 1]:
        return "Paper"

    elif fingers == [0, 1, 1, 0, 0]:
        return "Scissors"

    return "Unknown"


def computer_choice():

    import random

    choices = ["Rock", "Paper", "Scissors"]

    return random.choice(choices)


def find_winner(player, computer):

    if player == computer:
        return "Draw"

    elif player == "Rock" and computer == "Scissors":
        return "You Win!"

    elif player == "Paper" and computer == "Rock":
        return "You Win!"

    elif player == "Scissors" and computer == "Paper":
        return "You Win!"

    return "Computer Wins!"


def check_game_over(player_score, computer_score):

    if player_score >= 3:
        return "YOU WIN THE GAME!"

    elif computer_score >= 3:
        return "COMPUTER WINS THE GAME!"

    return ""
