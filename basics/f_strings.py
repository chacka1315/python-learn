person = "Siaka"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
print(message)

player = {"person": "Siaka", "coins": "Unlimited"}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

# f-strings
message = f"\n{person} has {coins * 5} coins left"
print(message)

message = f"\n{person.upper()} has {coins * 5} coins left"
print(message)

num = 10
foo = "foo"
bar = "bar"
print(f"\n2.25 times {num} = {2.25*10:.2f}")  # 2f = JSnumb.toFixed(2)
for i in range(0, 11):
    print(f"{i} times 9 = {9*i}")
