def greetPerson(name):
    print("Hello ", name, "!")


def sum(num1, num2):
    return num1 + num2


def double(num):
    return num * 2


def addTen(num):
    return num + 10


def sumDoubleAddTen(num1=0, num2=0):
    if type(num1) != int or type(num2) != int:
        return 0
    return addTen(double(sum(num1, num2)))


print(sumDoubleAddTen(7, 3))
print(sumDoubleAddTen())
print(sumDoubleAddTen("a", "b"))


def multipleItems(*args):
    print(type(args), args)  # tuples


def mul_named_rgs(**kwargs):
    print(type(kwargs), kwargs)  # dict


multipleItems(1, 2, 3)
mul_named_rgs(one=1, two=2)
