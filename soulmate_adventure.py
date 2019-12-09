import time
import random
woman = random.choice([
    "a princess", "a beautiful woman", "a top model", "Adriana Lima"])
gifts = random.choice([
    "necklace", "gold ring", "diamond ring", "iPhone11", "Macbook"])
character = random.choice([
    "Mysterious man", "Old woman", "A stranger"])


def print_pause(message_to_print):
    print(message_to_print)
    time_to_sleep = 2
    time.sleep(time_to_sleep)


def intro():
    print_pause("You find yourself in the street.")
    print_pause(
        "In front of you are there are a house, a shop "
        "and a bank\n")
    print_pause(
        character + " come to you and says " + woman +
        " living in the house.\n"
        "You must see her. Maybe she is your soulmate :) \n")


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_pause("Please choose a valid number")
    return response


def play_again():
    while True:
        response = input(
            "Would you like to play again?"
            " Please say 'yes' or 'no'.\n").lower()
        if "no" in response:
            print_pause("OK, goodbye!")
            break
        elif "yes" in response:
            print_pause("Good, let's play again :)")
            play_game()
        else:
            print("Sorry, I don't understand.")


def bank(items):
    print_pause(
        "You entered the bank.\n"
        "You entered the line. You have to wait.\n")
    if "money" in items:
        print_pause(
            "After some waiting, it's your turn.\n"
            "The banker smiling to you. Poor boy! Your balance is zero! "
            "Nothing to do here.")

    else:
        print_pause(
            "After some waiting, it's your turn.\n"
            "The banker smiling to you.\n"
            "Good. Now you took all of your money in your account.\n")
        items.append("money")
    print_pause("You head back to street.")
    choose_place(items)


def shop(items):
    print_pause(
        "You walked and entered the shop.\n"
        "You can buy the gift and win her heart :)\n")
    if "gift" in items:
        print_pause(
            "Shopkeeper welcomes you and say: \n"
            "'Nice to see you again'")
        print_pause(
            "But sadly you can't buy more gift. \n"
            "Did you forget?"
            "You spend all of your money."
            "Nothing to do more here.")
    else:
        print_pause("Shopkeeper welcomes you.")
        if "money" in items:
            print_pause("He showed gifts.\n")
            print_pause(
                "And you spend all of your money in a "
                + gifts + "!!\n")
            items.append("gift")
        else:
            print_pause(
                "You want to buy a gift. But how you will pay? \n"
                "You don't have any money.")
    print_pause("You head back to street.")
    choose_place(items)


def choose_place(items):
    place = valid_input(
        "Please enter the number of your place "
        "would you like the enter:\n 1.bank\n 2.shop\n 3.house\n"
        " Please enter 1, 2 or 3\n", "1", "2", "3")
    if place == '1':
        bank(items)
    elif place == '2':
        shop(items)
    elif place == '3':
        house(items)


def house(items):
    print_pause("You came to the house.")
    print_pause("You will see " + woman + "!!")
    print_pause("You are very excited, your heartbeat like crazy!!")
    if "gift" in items:
        print_pause("She looked from peep scope and opened the door")
        response = valid_input(
            "What you will do now? \n"
            "1. Say; you are very beautiful\n"
            "2. Don't say anything. Kiss her!! \n"
            "3. Say; Well, here I am. What were your other two wishes? \n"
            "Please enter 1,2 or 3\n", "1", "2", "3")
        if response == "1":
            print_pause(
                "This didn't impress her at all. She closed door. "
                "You lost her. Also the game..")
            play_again()
        elif response == "2":
            print_pause(
                "She pushed you immediately. And closed door. "
                "Are you pervert or what!?\n"
                "You lost her. Also the game..")
            play_again()
        elif response == "3":
            print_pause(
                "Your words smiled her. Also she saw your gift.\n"
                "Her face became blush. " "She loved " + gifts +
                " She hug you and kiss you!!\n")
            print_pause("You won her heart <3 Also the game :)\n")
            play_again()
    else:
        print_pause("She looked from peep scope. \n")
        print_pause("She didn't open the door. There must be a way..\n")
        print_pause("You return to the street..\n")
        choose_place(items)


def play_game():
    items = []
    intro()
    choose_place(items)


play_game()
