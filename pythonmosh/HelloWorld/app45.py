phone_number = input("Phone: ")

digits_name = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}

output = ""

for character in phone_number:
    output += digits_name.get(character, "!") + " "
print(output)