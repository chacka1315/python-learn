import math

# string
first = "Siaka"
last = "Billionaire"
print(type(first))
print(type(first) == str)
print(isinstance(last, str))
chocolate = str("Black")
print(type(chocolate))
print(type(chocolate) == str)
print(isinstance(chocolate, str))

full = first + " " + last
print(full)
full += "!"

# casting
year = str(1980)
phrase = "Love money since " + year + " 's."
print(phrase)

# multiple line
multiline = """
Hey Guy


How Are you!
"""
print(multiline)

# escaping
sentence = "I'm Siaka, a fancy billionaire\t and love nutrition\n Love Money\nLocated in US/California"
print(sentence)
print(first.lower())
print(first.upper())
print(multiline.title())  # uppercase first letters
print(sentence.replace("Money", "FREEDOM"))
print(len(multiline))
print(multiline.strip())  ##trim() in js
print(sentence.find("a"))
print("Siaka".center(19, "*"))
print("Black chocolate".ljust(40, "-") + "$5".rjust(4))

# string index
print(first[0])
print(first[1:-1])  # index not included

# str methods return boolean
print(first.endswith("a"))
print(first.startswith("S"))

# boolean data types
print("Boolean data types".center(40, "*"))
mybool = True
x = bool(False)
print(type(mybool), isinstance(x, bool))

# numeeric data types
print("Numeric data types".center(40, "*"))
price = 300_000
quantity = int(5)
print(price, type(price))
gpa = 4.99
print(abs(-12))
print(round(gpa, 1))
print(math.pi)
print(math.sqrt(2))
print(math.ceil(gpa))  # Neer the highest integer
print(math.floor(gpa))  # Neer the smallest integer
zipcode = "1980"
zip_value = int(zipcode)
print(zip_value)

# complex_type
comp_value = 5j
comp_value2 = 2j + 1
print(comp_value.real)
print(comp_value2.imag)
