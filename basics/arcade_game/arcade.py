import argparse
import rps
import guess_number as rmn
import sys


def arcade(player_name="Player"):

    print(f"\nWelcome to our arcade {player_name}!")

    def play_game():
        play_again = True

        while play_again:
            ply_choice = input(
                f"\n{player_name}, choose a game:\n\n==> 1 for Rocks Paper Scissors,\n==> 2 for Guess my number,\n==> x to quit\n\nChoice: "
            )

            choices = ["1", "2", "x"]

            while ply_choice not in choices:
                ply_choice = input("\nYou might enter 1, 2 or x!\nChoice: ")

            ply_choice = ply_choice.lower()

            if ply_choice == "1":
                rps_game = rps.rock_paper_sc(player_name)
                rps_game()
            elif ply_choice == "2":
                gmn_game = rmn.guess_my_numb(player_name)
                gmn_game()
            elif ply_choice == "x":
                sys.exit(f"\nSee you next time, {player_name}, hope you enjoyed!")
                play_again = False

    play_game()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide a personal experience.")
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the player.",
    )
    args = parser.parse_args()
    player_name = args.name
    arcade(player_name)
