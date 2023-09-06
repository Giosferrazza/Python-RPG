def start_game():
    print("You wake up in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r) ")
    answer = input()
    if answer == "l":
        print("You go left and are eaten by a grue. The end.")
    elif answer == "r":
        right_room()

def right_room():
        print("You go through the door on the right and see a lady crying on the floor.")
        print("What do you do?")
        print("1. Ask her what's wrong.")
        print("2. Run away.")
        answer = input()
        if answer == "1":
            print("She tells you she is crying because she is lost and her family was eaten by a grue.")
        elif answer == "2":
            print("You run away and fall into a pit. The end.")
        else:
            print("Invalid input.")


def get_name():
    name = input("What is your name? ")
    print("Hello, " + name)


def main():
    get_name()
    start_game()



if __name__ == "__main__":
    main()