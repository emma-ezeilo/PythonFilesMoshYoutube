# Creating a reusable function

def emoji_converter(message):
    emoji_symbols = message.split()
    emojis = {
        ":)": "Smiley Face",
        ":(": "Depressed Face"
    }
    output = ""
    for emoji_symbols1 in emoji_symbols:
        output += emojis.get(emoji_symbols1, emoji_symbols1) + " "
    return output


message = input(">")
print(emoji_converter(message))
