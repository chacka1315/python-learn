import argparse


def greet(name, lang="EN"):
    greetings = {"EN": "Hello", "FR": "Salut", "SP": "Hola"}
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide a personal greeting.")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet.",
    )

    parser.add_argument(
        "-l",
        "--lang",
        metavar="lang",
        required=False,
        choices=["EN", "FR", "SP"],
        help="The lamnguage in wich we greet.",
    )
    args = parser.parse_args()

    if args.__contains__("lang"):
        greet(args.name, args.lang)
    else:
        print("No lang")
        greet(args.name)
