users = ["Siaka", "Money", "Freedom"]

print(users)
print("Siaka" in users)
print(users[-1])  # last value
print(users.index("Freedom"))
print(len(users))  # last value
users += ["Traveling"]
users.extend(["Adventurer"])
print(users)

users.insert(0, "stoic")  # insert at the start
print(users)

# users.remove("Traveling")
# print(users.pop())

# del users[-1]
# print(users)

# users.clear()
# print(users)

users.sort()
print(users)

nums = [4, 44, 8, 0, 2]
print(type(nums))
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))  # sort but not modifie the original list

numsCopy = nums.copy()  # copy
myNumsCopy = list(nums)  # also copy
myCopy = nums[:]
myNumsChunk = nums[1:3]
print(numsCopy, myNumsCopy, myCopy, myNumsChunk)

# tuples
myTuple = tuple(("Siaka", 42, True))
tuple2 = ("Siaka", "the", "billionaire")
print(type(myTuple), type(tuple2))
print(tuple2, myTuple)
tupleList = list(myTuple)
tupleList.append(False)
myTuple = tuple(tupleList)
print(myTuple)

# destructuring
(*one, two, rest) = myTuple
print(one, two, rest)
val = ["foo", "bar", "baz"]
[foo, *noFoo] = val
print(foo, noFoo)
