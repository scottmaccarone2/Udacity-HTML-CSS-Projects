# The code below was my FIRST attempt to replicate the `elevator` example given by Udacity. I was attempting to match the outward behavior of the program. This first attempt is actually quite good, though I should probably write a `valid_input()` function. A simplier program can be done with `while` loops, but I wanted to practice using functions and composition of functions.

# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(2)
#
# def intro():
#     greeting = ["You have just arrived at your new job!",
#                 "You are in the elevator."]
#     for item in greeting:
#         print_pause(item)
#
# # def valid_input(value):
# #     pass
#
# def floor_choice():
#     print_pause("Please enter the number for the floor you would like to visit:")
#     response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#     if response == 1:
#         print_pause("You push the button for the first floor.")
#         print_pause("After a few moments, you find yourself in the lobby.")
#     elif response == 2:
#         print_pause("You push the button for the second floor.")
#         print_pause("After a few moments, you find yourself in the human resources department.")
#     elif response == 3:
#         print_pause("You push the button for the third floor.")
#         print_pause("After a few moments, you find yourself in the engineering department.")
#
#     print_pause("Where would you like to go next?")
#     floor_choice()
#
#
# def elevator():
#     intro()
#     floor_choice()
#
# elevator()

#-------------------------------------------------------------------------

# Below is a simplier version of the above program:

# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(2)
#
# print_pause("You have just arrived at your new job!")
# print_pause("You are in the elevator.")
#
# while True:
#     print_pause("Please enter the number for the floor you would like to visit:")
#     response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#     if response == 1:
#         print_pause("You push the button for the first floor.")
#         print_pause("After a few moments, you find yourself in the lobby.")
#     elif response == 2:
#         print_pause("You push the button for the second floor.")
#         print_pause("After a few moments, you find yourself in the human resources department.")
#     elif response == 3:
#         print_pause("You push the button for the third floor.")
#         print_pause("After a few moments, you find yourself in the engineering department.")
#
#     print_pause("Where would you like to go next?")

#-------------------------------------------------------------------------

# Now I build a game. The goal is to make it to the third floor to start a new job. The user must obtain certain items before access is granted to the third floor:
# First floor: obtain ID card
# Second floor: obtain the employee handbook, but only if you have an ID card
# Third floor: get to work, but only if you have BOTH the ID card and employee handbook
# This first iteration of the game builds the first floor. I might use the simplier `elevator` code from above (without the use of many functions) and refactor later...

# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(1)
#
# print_pause("You have just arrived at your new job!")
# print_pause("You are in the elevator.")
#
# item_list = []
# while True:
#     print_pause("Please enter the number for the floor you would like to visit:")
#     response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#     if response == 1:
#         print_pause("You push the button for the first floor.")
#         print_pause("After a few moments, you find yourself in the lobby.")
#         if "ID card" in item_list:
#             print_pause("The clerk greets you, but he has already given you your ID card, so there is nothing more to do here now.")
#         else:
#             item_list.append("ID card")
#             print_pause("The clerk greets you and gives you your ID card.")
#     elif response == 2:
#         print_pause("You push the button for the second floor.")
#         print_pause("After a few moments, you find yourself in the human resources department.")
#     elif response == 3:
#         print_pause("You push the button for the third floor.")
#         print_pause("After a few moments, you find yourself in the engineering department.")
#
#     print_pause("Where would you like to go next?")

#-------------------------------------------------------------------------

# My first attempt at including the first floor ID card addition:

# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(1)
#
# def intro():
#     greeting = ["You have just arrived at your new job!",
#                 "You are in the elevator."]
#     for item in greeting:
#         print_pause(item)
#
# # def valid_input(value):
# #     pass
#
# item_list = []
# def floor_choice():
#     print_pause("Please enter the number for the floor you would like to visit:")
#     response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#     if response == 1:
#         print_pause("You push the button for the first floor.")
#         print_pause("After a few moments, you find yourself in the lobby.")
#         if "ID card" in item_list:
#             print_pause("The clerk greets you, but he has already given you your ID card, so there is nothing more to do here now.")
#         else:
#             item_list.append("ID card")
#             print_pause("The clerk greets you and gives you your ID card.")
#     elif response == 2:
#         print_pause("You push the button for the second floor.")
#         print_pause("After a few moments, you find yourself in the human resources department.")
#     elif response == 3:
#         print_pause("You push the button for the third floor.")
#         print_pause("After a few moments, you find yourself in the engineering department.")
#
#     print_pause("Where would you like to go next?")
#     floor_choice()
#
#
# def elevator():
#     intro()
#     floor_choice()
#
# elevator()

#-------------------------------------------------------------------------

# Now we begin to build the second floor where the user obtains the employee handbook but only if he has the ID card:

# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(1)
#
# print_pause("You have just arrived at your new job!")
# print_pause("You are in the elevator.")
#
# item_list = []
# while True:
#     print_pause("Please enter the number for the floor you would like to visit:")
#     response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#     if response == 1:
#         print_pause("You push the button for the first floor.")
#         print_pause("After a few moments, you find yourself in the lobby.")
#         if "ID card" in item_list:
#             print_pause("The clerk greets you, but he has already given you your ID card, so there is nothing more to do here now.")
#         else:
#             item_list.append("ID card")
#             print_pause("The clerk greets you and gives you your ID card.")
#     elif response == 2:
#         print_pause("You push the button for the second floor.")
#         print_pause("After a few moments, you find yourself in the human resources department.")
#         if "EE handbook" in item_list:
#             print_pause("The HR folks are busy at their desks.")
#             print_pause("There doesn't seem to be much to do here.")
#         else:
#             print_pause("The HR manager greets you.")
#             if "ID card" in item_list:
#                 item_list.append("EE handbook")
#                 print_pause("He looks at your ID card and then gives you a copy of the Employee Handbook.")
#             else:
#                 print_pause("He has something for you, but says he can't give it to you until you get your ID card.")
#     elif response == 3:
#         print_pause("You push the button for the third floor.")
#         print_pause("After a few moments, you find yourself in the engineering department.")
#
#     print_pause("Where would you like to go next?")

#-------------------------------------------------------------------------

# I now build out the third floor where the user attempts to enter the office. If the user has the ID card, they may open the door; otherwise, they are told the door is locked and head back tot he elevator. If the user has both the ID card and EE handbook, the user wins; otherwise (the user has the ID card, but NOT the handbook), the user is sent back to the elevator.

# The code below is fully functional and works as desired!

# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(1)
#
# print_pause("You have just arrived at your new job!")
# print_pause("You are in the elevator.")
#
# item_list = []
# while True:
#     print_pause("Please enter the number for the floor you would like to visit:")
#     response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#     if response == 1:
#         print_pause("You push the button for the first floor.")
#         print_pause("After a few moments, you find yourself in the lobby.")
#         if "ID card" in item_list:
#             print_pause("The clerk greets you, but he has already given you your ID card, so there is nothing more to do here now.")
#         else:
#             item_list.append("ID card")
#             print_pause("The clerk greets you and gives you your ID card.")
#     elif response == 2:
#         print_pause("You push the button for the second floor.")
#         print_pause("After a few moments, you find yourself in the human resources department.")
#         if "EE handbook" in item_list:
#             print_pause("The HR folks are busy at their desks.")
#             print_pause("There doesn't seem to be much to do here.")
#         else:
#             print_pause("The HR manager greets you.")
#             if "ID card" in item_list:
#                 item_list.append("EE handbook")
#                 print_pause("He looks at your ID card and then gives you a copy of the Employee Handbook.")
#             else:
#                 print_pause("He has something for you, but says he can't give it to you until you get your ID card.")
#     elif response == 3:
#         print_pause("You push the button for the third floor.")
#         print_pause("After a few moments, you find yourself in the engineering department.")
#         if "ID card" in item_list:
#             print_pause("You use your ID card to open the door. Your program manager greets you and tells you that you need a copy of the employee handbook in order to start work.")
#             if "EE handbook" in item_list:
#                 print_pause("Fortunately, you got that from HR! Congratulations! You are ready to start your new job as vice president of engineering!")
#                 break
#             else:
#                 print_pause("He scowls when he sees you don't have it, and sends you back to the elevator.")
#         else:
#             print_pause("Unfortunately, the door is locked and you can't get in. It looks like you need some kind of key card to open the door. You head back to the elevator.")
#
#     print_pause("Where would you like to go next?")

#-------------------------------------------------------------------------

# Now I make the effort to refactor the code above. There are a LOT of conditionals and repeated calls/code pieces.
# First, I'll define functions for each floor separately, then call these functions within the larger program (while loop) as appropriate.
# NOTE: There is a problem with the thrid floor function! Since the break statement can no longer exist in the `third_floor()` function, we have no way of breaking out of our loop! Thus, this program will continue forever! This will be fixed in the next iteration of refactoring. Most likely, I will remove the `while` loop altogether and use composition of functions somehow.

# import time
# item_list = []
#
#
# def print_pause(s):
#     print(s)
#     time.sleep(1)
#
#
# def first_floor():
#     print_pause("You push the button for the first floor.")
#     print_pause("After a few moments, you find yourself in the lobby.")
#     if "id" in item_list:
#         print_pause("The clerk greets you, but he has already given you your ID card, so there is nothing more to do here now.")
#     else:
#         item_list.append("id")
#         print_pause("The clerk greets you and gives you your ID card.")
#
#
# def second_floor():
#     print_pause("You push the button for the second floor.")
#     print_pause("After a few moments, you find yourself in the human resources department.")
#     if "handbook" in item_list:
#         print_pause("The HR folks are busy at their desks.")
#         print_pause("There doesn't seem to be much to do here.")
#     else:
#         print_pause("The HR manager greets you.")
#         if "id" in item_list:
#             item_list.append("handbook")
#             print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
#         else:
#             print_pause("He has something for you, but says he can't give it to you until you get your ID card.")
#
#
# def third_floor():
#     print_pause("You push the button for the third floor.")
#     print_pause("After a few moments, you find yourself in the engineering department.")
#     if "id" in item_list:
#         print_pause("You use your ID card to open the door.")
#         print_pause("Your program manager greets you and tells you that you need a copy of the employee handbook in order to start work.")
#         if "handbook" in item_list:
#             print_pause("Fortunately, you got that from HR!")
#             print_pause("Congratulations! You are ready to start your new job as vice president of engineering!")
#         else:
#             print_pause("He scowls when he sees you don't have it, and sends you back to the elevator.")
#     else:
#         print_pause("Unfortunately, the door is locked and you can't get in.")
#         print_pause("It looks like you need some kind of key card to open the door.")
#         print_pause("You head back to the elevator.")
#
#
# def elevator():
#     while True:
#         print_pause("Please enter the number for the floor you would like to visit:")
#         response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#         if response == 1:
#             first_floor()
#         elif response == 2:
#             second_floor()
#         elif response == 3:
#             third_floor()
#         print_pause("Where would you like to go next?")
#
#
# elevator()

#-------------------------------------------------------------------------

# In this solution, we call the `elevator()` function each time we need the user to get back on the elevator. Thus, we eliminate the while loop, and simply do NOT call the `elevator()` function when the user wins the game!

# import time
# item_list = []
#
#
# def print_pause(s):
#     print(s)
#     time.sleep(1)
#
#
# def intro():
#     print_pause("You have just arrived at your new job!")
#     print_pause("You are in the elevator.")
#
#
# def first_floor():
#     print_pause("You push the button for the first floor.")
#     print_pause("After a few moments, you find yourself in the lobby.")
#     if "id" in item_list:
#         print_pause("The clerk greets you, but he has already given you your ID card, so there is nothing more to do here now.")
#     else:
#         item_list.append("id")
#         print_pause("The clerk greets you and gives you your ID card.")
#     print_pause("Where would you like to go next?")
#     elevator()
#
#
# def second_floor():
#     print_pause("You push the button for the second floor.")
#     print_pause("After a few moments, you find yourself in the human resources department.")
#     if "handbook" in item_list:
#         print_pause("The HR folks are busy at their desks.")
#         print_pause("There doesn't seem to be much to do here.")
#     else:
#         print_pause("The HR manager greets you.")
#         if "id" in item_list:
#             item_list.append("handbook")
#             print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
#         else:
#             print_pause("He has something for you, but says he can't give it to you until you get your ID card.")
#     print_pause("Where would you like to go next?")
#     elevator()
#
#
# def third_floor():
#     print_pause("You push the button for the third floor.")
#     print_pause("After a few moments, you find yourself in the engineering department.")
#     if "id" in item_list:
#         print_pause("You use your ID card to open the door.")
#         print_pause("Your program manager greets you and tells you that you need a copy of the employee handbook in order to start work.")
#         if "handbook" in item_list:
#             print_pause("Fortunately, you got that from HR!")
#             print_pause("Congratulations! You are ready to start your new job as vice president of engineering!")
#         else:
#             print_pause("He scowls when he sees you don't have it, and sends you back to the elevator.")
#             print_pause("Where would you like to go next?")
#             elevator()
#     else:
#         print_pause("Unfortunately, the door is locked and you can't get in.")
#         print_pause("It looks like you need some kind of key card to open the door.")
#         print_pause("You head back to the elevator.")
#         print_pause("Where would you like to go next?")
#         elevator()
#
#
# def elevator():
#     print_pause("Please enter the number for the floor you would like to visit:")
#     response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
#     if response == 1:
#         first_floor()
#     elif response == 2:
#         second_floor()
#     elif response == 3:
#         third_floor()
#
#
# intro()
# elevator()

#-------------------------------------------------------------------------

# Aside from the `import time` statement, there are only 3 lines of code that are outside function definitions:
# item_list = [] ---- empty list
# intro() ---- function call
# elevator() ---- function call
# I'll place these three lines of code in a `play_game()` function, and call that function at the bottom of the file.
# However, the `item_list` variable will then be considered a LOCAL variable within the `play_game()` function, and will therefore NOT be seen by other functions! Thus, we need to pass the `item_list` variable in as arguments to the appropriate functions that require it.
# NOTE: Udacity uses the same `item_list` variable in ALL the function calls and function definitions! I think this is overkill, and in fact, I'm not sure it would work. I simply defined my functions with a general `list` parameter, and this general list object is used throughout all the function defintions. The only time I actually need to use `item_list` is in the `play_game()` function definition!

import time


def print_pause(s):
    print(s)
    time.sleep(1)


def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def first_floor(list):
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find yourself in the lobby.")
    if "id" in list:
        print_pause("The clerk greets you, but he has already given you your ID card, so there is nothing more to do here now.")
    else:
        list.append("id")
        print_pause("The clerk greets you and gives you your ID card.")
    print_pause("Where would you like to go next?")
    elevator(list)


def second_floor(list):
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself in the human resources department.")
    if "handbook" in list:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The HR manager greets you.")
        if "id" in list:
            list.append("handbook")
            print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
        else:
            print_pause("He has something for you, but says he can't give it to you until you get your ID card.")
    print_pause("Where would you like to go next?")
    elevator(list)


def third_floor(list):
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself in the engineering department.")
    if "id" in list:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells you that you need a copy of the employee handbook in order to start work.")
        if "handbook" in list:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulations! You are ready to start your new job as vice president of engineering!")
        else:
            print_pause("He scowls when he sees you don't have it, and sends you back to the elevator.")
            print_pause("Where would you like to go next?")
            elevator(list)
    else:
        print_pause("Unfortunately, the door is locked and you can't get in.")
        print_pause("It looks like you need some kind of key card to open the door.")
        print_pause("You head back to the elevator.")
        print_pause("Where would you like to go next?")
        elevator(list)


def elevator(list):
    print_pause("Please enter the number for the floor you would like to visit:")
    response = int(input("1. Lobby\n2. Human resources\n3. Engineering department\n"))
    if response == 1:
        first_floor(list)
    elif response == 2:
        second_floor(list)
    elif response == 3:
        third_floor(list)


def play_game():
    item_list = []
    intro()
    elevator(item_list)


play_game()
