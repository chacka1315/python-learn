import random
from enum import Enum
import sys


def rock_paper_sc(player_name="Player"):
    choices = {1: "ROCK 💎", 2: "PAPER 📃", 3: "SCISSORS ✂️"}
    game_count = 0
    win_count = 0

    class Status(Enum):
        WIN = 2
        DRAW = 1
        LOSE = 0

    def check_win(ply_choice, cpt_choice):
        if ply_choice == 1 and cpt_choice == 3:
            return Status.WIN
        elif ply_choice == 2 and cpt_choice == 1:
            return Status.WIN
        elif ply_choice == 3 and cpt_choice == 2:
            return Status.WIN
        elif ply_choice == cpt_choice:
            return Status.DRAW
        else:
            return Status.LOSE

    def print_status_msg(status):
        nonlocal win_count
        nonlocal game_count
        game_count += 1
        if status == Status.WIN:
            print(f"{player_name}You win! 🎉")
            win_count += 1
        elif status == Status.DRAW:
            print("Tie game! 🤯")
        else:
            print("Computer win! 🤖")

    def print_game_stats():
        print(f"Game count: {game_count}")
        print(f"Wins count: {win_count}")
        print(f"Percentage of wins: {win_count/game_count:.2%}")

    def play():
        print("")
        print(f" ROUND {game_count+1} ".center(40, "*"))
        ply_choice = input(
            f"\n{player_name}, enter your choice:\n💎 1 for Rocks,\n📃 2 for Paper,\n✂️  3 for Scissors\nChoice: "
        )

        while int(ply_choice) not in choices:
            ply_choice = input("\nYou might enter 1, 2 or 3!\nChoice: ")

        ply_choice = int(ply_choice)
        cpt_choice = random.choice("123")
        cpt_choice = int(cpt_choice)

        print(f"\n{player_name}, you choose: {choices.get(ply_choice)}")
        print(f"Computer choose: {choices[cpt_choice]}\n")
        status = check_win(ply_choice, cpt_choice)
        print_status_msg(status)
        print_game_stats()

    def starts_rps():
        play_again = True
        while play_again:
            play()

            anwser = input(
                f"\n{player_name}, do you want to play again?\nEnter Y to play again or\nQ to quit the game: "
            )

            if anwser.lower() == "y":
                continue
            else:
                print(f"\nBye {player_name}! 🙌")
                play_again = False

    return starts_rps


# rps = rock_paper_sc("Siaka")
