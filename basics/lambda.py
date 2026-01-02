from functools import reduce

# lambda functions
addTwo = lambda num: num + 2
print(addTwo(10))

sumThree = lambda a, b, c: a + b + c
print(sumThree(2, 3, 4))


############################
def fnBuilder(x):
    return lambda num: num + x


addTen = fnBuilder(10)
print(addTen(15))

###########################
squared = lambda num: num * num
nums = [4, 9, 3, 10, 15, 100]


def compute_list(nums_list, fn):
    return [fn(num) for num in nums_list if num != 10]


# map(fn, iterrable)
squared_nums = map(squared, nums)
print(list(squared_nums))

# filter(fn, iterrable)
odd_nums = filter(lambda num: num % 2 != 0, nums)
print(list(odd_nums))


# reduce(fn, iterrable)
def func(acc, curr):
    return acc + curr


# list_sum = reduce(func, nums, 100)

list_sum = reduce(lambda curr, acc: acc + curr, nums, 100)
another_sum = sum(nums, 100)

print(list_sum, another_sum)
