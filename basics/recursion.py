def add_one(num):
    if num == 10:
        return num
    total = num + 1
    print(total)

    return add_one(total)


print("RES: ", add_one(10))
