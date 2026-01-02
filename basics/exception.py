x = 2


class MyException(Exception):
    pass


try:
    # if type(x) is not str:
    #     raise TypeError("Only numbers are allowed!")

    # print(x)
    raise MyException("Just not cool Error")
except NameError:
    print("Name Error")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as error:
    print(error)
else:
    print("No error occured")
finally:
    print("Print anyway")
