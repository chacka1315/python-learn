# value = 1
# while value < 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)

cars = ["Lamborghini", "Rolce Roys", "Bugatti", "Ferrari"]

# for car in cars:
#     if car.startswith("Bu"):
#         break
#     print(car)
#     for letter in car:
#         print(letter)
#         if letter == "a":
#             break

# for car in cars:
#     if car != "Ferrari":
#         continue
#     print(car)

for i in range(4):
    print(i)

print("+++")

for i in range(2, 4):
    print(i)
else:
    print("Out of range")

print("+++")

for i in range(0, 11, 2):
    print(i)

names = ["Siaka", "Naval", "Felix"]
industries = ["magazine", "tech"]

for name in names:
    for industry in industries:
        print(name + " ==> " + industry)
