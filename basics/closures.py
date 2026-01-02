def parent_fn(person, coins=3):
    def check_coins():
        if coins > 1:
            print("\n", person, " has ", coins, " coins left.")
        elif coins == 1:
            print("\n", person, " has ", coins, " coin left.")
        else:
            print("\n", person, " is out of coins!")

    def play():
        nonlocal coins
        coins -= 1
        check_coins()

    return play


felix = parent_fn("Felix", 10)

felix()
felix()
felix()
