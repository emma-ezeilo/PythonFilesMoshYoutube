# This is an emoji converter
message = input("> ")
words = message.split()
emojis = {
    ":)":"Smiley face",
    ":(":"Depressed face"
}
output = ""
for word in words:
    output += emojis.get(word, word)
print(output)
