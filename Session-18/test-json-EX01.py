import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX1.json").read_text()

person = json.loads(jsonstring)

print()

names = person["Name"]
#NAMES: [{'Firstname': 'Troll', 'Lastname': 'Face'}, {'Firstname': 'Sax', 'Lastname': 'Guy'}]

ages = person["age"]

phonenumbers = person["phoneNumber"]
print("------PHONENUMBERS: ", phonenumbers)

termcolor.cprint("Total people in the data base: ", 'green', end='')
print(len(names))

for i, name in enumerate(names):

    termcolor.cprint("Name:", 'green', end="")
    print(name["Firstname"], name["Lastname"])

    termcolor.cprint("Age:", 'green', end="")
    print(ages[i])

    for n, num in enumerate(phonenumbers):
        if num["number"][i] == "0":
            pass
        else:
            termcolor.cprint("  Phone {}:".format(n), 'blue')
            termcolor.cprint("    Type: ", 'red', end='')
            print(num["type"])
            termcolor.cprint("    Number: ", 'red', end='')
            print(num["number"][i])
