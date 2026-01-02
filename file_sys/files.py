# Read - error if it doesn't exist
import os
from pathlib import Path

# a append
# r read
# x create
# w write


# print(f.read())
# print(f.read(4)) # 4 means first fore letters
# print(f.readline())

try:
    f = open("names.txt")
    print(f.read())
    for line in f:
        print(line)
except Exception as error:
    print(error)
finally:
    f.close()

# Append - creates if not exists
try:
    f = open("names.txt", "a")
    f.write("\nDeutch")
except:
    print("No such file in dir.")
finally:
    f.close()

# Write (overwrite)
try:
    f = open("context.txt", "w")
    f.write("\nOverwriting context filess.")
except Exception as error:
    print(error)
finally:
    f.close()


# Write or create file if does not exist
try:
    f = open("context_new.txt", "w")
    f.write("\nNew file filess.")
except Exception as error:
    print(error)
finally:
    f.close()

# create but throw if exist
try:
    if not os.path.exists("siaka.py"):
        f = open("siaka.py", "x")
        code = open("files.py")
        f.write(code.read())
except Exception as error:
    print(error)
finally:
    f.close()

# deleting files
if os.path.exists("context_new.txt"):
    os.remove("context_new.txt")
else:
    print("Cannot find this file for deletion")

with open("names.txt") as f:
    content = f.read()

with open("more_names.txt", "a") as f:
    f.write(content)
