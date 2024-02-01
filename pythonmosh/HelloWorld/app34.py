# This is a car game without a GUI
print("This is a car game without a GUI")
command = ""

started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car has already started")
        else:
            started = True
            print("The car started ")
    elif command == "stop":
        if not started:
            print("The car has already stopped!")
        else:
            started = False
            print("The car has stopped ")
    elif command == "help":
        print("""start-starts the car
stop-stops the car
quit-quits the game
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand what you are typing \n Type help for options")
