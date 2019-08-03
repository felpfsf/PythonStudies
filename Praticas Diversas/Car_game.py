command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started :
            print("car is already started...")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped...")
        else:
            started = False
            print("Car stopped...")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("Sorry, I don't understand that")