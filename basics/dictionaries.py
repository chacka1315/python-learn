user = {"name": "Siaka", "age": 3}

user2 = dict(name="Ouatt", age=25)
print(type(user))
print(user, user2)

# items access
print(user["name"])
print(user.get("age"))
print("name" in user)  # true
print("Age" in user)  # false

# list keys, values
print(user.keys())
print(user.values())
print(user.items())

# change value
user2["status"] = "billionaire"  # new key
user2["location"] = "California, US"  # new key
user2["name"] = "Siaka"  # change value
user2.update({"wealth": "400B"})
print(user2)

# remove items
print(user2.pop("age"))
print(user2.popitem())
print(user2)
del user2["location"]
user.clear()
print(user, user2)
del user
# print(user)  # Error already deleted
user = user2  # copy per reference like in javascript
user = user2.copy()  # best copy!, new dictionary

entr1 = {"name": "Naval", "compagnies": {"first": "Epinions", "sec": "AngelList"}}

# nested access
print(entr1.get("compagnies").get("sec"))
print(entr1["compagnies"]["sec"])
print(entr1["compagnies"].get("first"))

# Sets
nums = {1, 2, 3, 4}
nums2 = set((5, 6, 7))
print(type(nums))
print(nums, nums2)
print(len(nums))

# not duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True = 1, 0 = False in Sets
nums = {1, True, 2, False, 0, 3}  # output: {False, 1, 2, 3}
print(nums)

# check if exist. but cannot access via index or keys like in list and dictionary
print(False in nums)
nums.add("Siaka")
nums.update({"Money"})
nums.update(["Freedom"])
print(nums)

nums3 = nums.union(nums2)
print(nums3)
nums3.intersection_update(nums)
print(nums3)
