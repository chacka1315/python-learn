import random
from enum import Enum


def guess_my_numb(player_name="Player"):
    choices = (1, 2, 3)
    game_count = 0
    win_count = 0

    def check_win(ply_choice, cpt_choice):
        nonlocal win_count
        nonlocal game_count
        game_count += 1

        if ply_choice == cpt_choice:
            print(f"{player_name}, you gess it, i had {cpt_choice} in mind! 🤩🎉")
            win_count += 1
        else:
            print(f"\nNope {player_name}, i had {cpt_choice} in mind! 🙃")
            print("Good luke for the next one!😉")

    def print_game_stats():
        print(f"\nGame count: {game_count}")
        print(f"Wins count: {win_count}")
        print(f"Percentage of wins: {win_count/game_count:.2%}")

    def play():
        print("")
        print(f" GUESS {game_count+1} ".center(40, "*"))
        ply_choice = input(f"\n{player_name}, enter your guess: 1, 2, 3\nChoice: ")

        while int(ply_choice) not in choices:
            ply_choice = input("\nYou might enter 1, 2 or 3!\nChoice: ")

        ply_choice = int(ply_choice)
        cpt_choice = random.choice("123")
        cpt_choice = int(cpt_choice)

        check_win(ply_choice, cpt_choice)
        print_game_stats()

    def starts_guess_my_num():
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

    return starts_guess_my_num


# gmn = guess_my_numb("Siaka")
# gmn()
