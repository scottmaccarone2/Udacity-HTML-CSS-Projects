# The first program to write is a breakfast bot that allows us to place a breakfast order (based on only two items). Before launching into code, there are some crucial pieces of the program we need to build:
# 1. Get input and use it to determine what happens next
# 2. Handle bad input without crashing
# 3. Be flexible with the input the user can enter
# 4. Print messages to the console, whith a short pause after each one
# 5. Allow the player to order again if they like

# import time

# def breakfast_bot():
#     order = (input("Please place your order. Would you like waffles or pancakes?\n"))
#     order = order.lower()
#     if order == 'waffles':
#         print('Waffles it is!')
#     elif order == 'pancakes':
#         print('Pancakes it is!')
#     else:
#         print("Sorry, I don't understand")


# breakfast_bot()

#---------------------------------------------------------------------------

# There needs to be a while loop so that if the user enters an invalid input, the program will not crash and will re-ask the question. There are two ways to do this (NOTE: I DID NOT COME UP WITH THESE - THESE WERE GIVE BY UDACITY INSTRUCTORS. I SHOULD HAVE BEEN ABLE TO COME UP WITH THESE SOLUTIONS ON MY OWN BUT I DID NOT):

# Method 1:
# def breakfast_bot1():
#     while True:
#         order = (input("Please place your order. Would you like waffles or pancakes?\n")).lower()
#         if order == 'waffles':
#             print('Waffles it is!')
#             break
#         elif order == 'pancakes':
#             print('Pancakes it is!')
#             break
#         else:
#             print("Sorry, that's not on our menu.")
#
# breakfast_bot1()

# Method 2:
# def breakfast_bot2():
#     order = ""
#     while order != 'waffles' and order != 'pancakes':
#         order = (input("Please place your order. Would you like waffles or pancakes?\n")).lower()
#         if order == 'waffles':
#             print('Waffles it is!')
#         elif order == 'pancakes':
#             print('Pancakes it is!')
#         else:
#             print("Sorry, I don't understand")
#
# breakfast_bot2()

#---------------------------------------------------------------------------

# Now modify the code so we can be flexible with a user input of something like:
# "I'd like waffles, please!"
# We need to use the `in` operator to check whether or not the string contains the 'waffles' or 'pancakes' keywords.

# def breakfast_bot1():
#     while True:
#         order = (input("Please place your order. Would you like waffles or pancakes?\n")).lower()
#         if 'waffles' in order:
#             print('Waffles it is!')
#             break
#         elif 'pancakes' in order:
#             print('Pancakes it is!')
#             break
#         else:
#             print("Sorry, that's not on our menu.")
#
# breakfast_bot1()

#---------------------------------------------------------------------------

# Now we will add messages to welcome the guest - but only the FIRST time the guest starts the bot(not with every order/re-order):

# NOTE: With SO many `time.sleep(2)` calls, we may want to rethink the structure of the program!

# def breakfast_bot1():
#     greeting = ["Hello, I am Bob, the Breakfast Bot.",
#                 "Today we have two breakfasts available.",
#                 "The first is waffles with strawberries and whipped cream.",
#                 "The second is sweet potato pancakes with butter and maple syrup."]
#     for item in greeting:
#         print(item)
#         time.sleep(2)
#
#     while True:
#         order = (input("Please place your order. Would you like waffles or pancakes?\n")).lower()
#         if 'waffles' in order:
#             print('Waffles it is!')
#             time.sleep(2)
#             break
#         elif 'pancakes' in order:
#             print('Pancakes it is!')
#             time.sleep(2)
#             break
#         else:
#             print("Sorry, that's not on our menu.")
#             time.sleep(2)
#
#     time.sleep(2)
#     print("Your order will be ready shortly.")
#
# breakfast_bot1()

#---------------------------------------------------------------------------

# We now need to allow the user to place additional orders. First, we must prompt the user and ask if they would like to order again. Depending on their response (yes or no), we write code for either scenario. If they say 'yes', we write code ask them to place the order; if they say 'no', the program should print a goodbye message and exit.

# Maybe use a nest while loop?

# def breakfast_bot1():
#     greeting = ["Hello, I am Bob, the Breakfast Bot.",
#                 "Today we have two breakfasts available.",
#                 "The first is waffles with strawberries and whipped cream.",
#                 "The second is sweet potato pancakes with butter and maple syrup."]
#     for item in greeting:
#         print(item)
#         time.sleep(2)
#
#     order_again = "yes"
#     while "yes" in order_again:
#         while True:
#             order = (input("Please place your order. Would you like waffles or pancakes?\n")).lower()
#             if 'waffles' in order:
#                 print('Waffles it is!')
#                 time.sleep(2)
#                 break
#             elif 'pancakes' in order:
#                 print('Pancakes it is!')
#                 time.sleep(2)
#                 break
#             else:
#                 print("Sorry, that's not on our menu.")
#                 time.sleep(2)
#
#         time.sleep(2)
#         print("Your order will be ready shortly.")
#         time.sleep(2)
#
#         while True:
#             order_again = (input("Would you like to place another order? Please say 'yes' or 'no'.\n")).lower()
#             time.sleep(2)
#             if 'yes' in order_again:
#                 print("Very good, I'm happy to take another order.")
#                 time.sleep(2)
#                 break
#             elif 'no' in order_again:
#                 print("OK, goodbye!")
#                 break
#             else:
#                 print("Sorry, I don't understand.")
#
# breakfast_bot1()

#---------------------------------------------------------------------------
# Write a print_pause() function that prints the given string/statement to the user, and then pauses for two seconds. Use this function to clean up the code above:

# def print_pause(s):
#     print(s)
#     time.sleep(2)
#
#
# def breakfast_bot1():
#     greeting = ["Hello, I am Bob, the Breakfast Bot.",
#                 "Today we have two breakfasts available.",
#                 "The first is waffles with strawberries and whipped cream.",
#                 "The second is sweet potato pancakes with butter and maple syrup."]
#     for item in greeting:
#         print_puase(item)
#
#     order_again = "yes"
#     while "yes" in order_again:
#         while True:
#             order = (input("Please place your order. Would you like waffles or pancakes?\n")).lower()
#             if 'waffles' in order:
#                 print_pause('Waffles it is!')
#                 break
#             elif 'pancakes' in order:
#                 print_pause('Pancakes it is!')
#                 break
#             else:
#                 print_pause("Sorry, that's not on our menu.")
#
#         print_pause("Your order will be ready shortly.")
#
#         while True:
#             order_again = (input("Would you like to place another order? Please say 'yes' or 'no'.\n")).lower()
#             time.sleep(2)
#             if 'yes' in order_again:
#                 print_pause("Very good, I'm happy to take another order.")
#                 break
#             elif 'no' in order_again:
#                 print_pause("OK, goodbye!")
#                 break
#             else:
#                 print_pause("Sorry, I don't understand.")
#
# breakfast_bot1()

#--------------------------------------------------------------------------

# Write a `valid_input()` function to simplify the code above:
# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(2)

# The goal of this function is to build on the `input()` function. Yes, we still want input from the user, but then we want to check if that input contains particular keywords. In the first case, we need to see if the users input contain "waffles" or "pancakes"; and in the second case, we want to check if the users input contains "yes" or "no".

# def valid_input(prompt, option1, option2):
#     while True:
#         user_response = input(prompt).lower()
#         if option1 in user_response:
#             return user_response
#         elif option2 in user_response:
#             return user_response
#         else:
#             print_pause("Sorry, I don't understand.")
#
# def breakfast_bot1():
#     greeting = ["Hello, I am Bob, the Breakfast Bot.",
#                 "Today we have two breakfasts available.",
#                 "The first is waffles with strawberries and whipped cream.",
#                 "The second is sweet potato pancakes with butter and maple syrup."]
#     for item in greeting:
#         print_pause(item)
#
#     order_again = "yes"
#     while "yes" in order_again:
#         order = (valid_input("Please place your order. Would you like waffles or pancakes?\n", "waffles", "pancakes"))
#         if 'waffles' in order:
#             print_pause('Waffles it is!')
#         elif 'pancakes' in order:
#             print_pause('Pancakes it is!')
#
#         print_pause("Your order will be ready shortly.")
#
#         order_again = (valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n", "yes", "no"))
#         if 'yes' in order_again:
#             print_pause("Very good, I'm happy to take another order.")
#         elif 'no' in order_again:
#             print_pause("OK, goodbye!")
#
# breakfast_bot1()

#--------------------------------------------------------------------------

# Now let's modify the `valid_input()` function so it can accept any number of options, not just two. That way, we can begin to build our menu to include bacon, eggs, crepes, etc. To do this, use a list that contains all the possible options. Then use a `for` loop to iterate over each item/option, and check that the option is in the user's input.

# import time
#
# def print_pause(s):
#     print(s)
#     time.sleep(2)
#
# def valid_input(prompt, option_list):
#     while True:
#         user_response = input(prompt).lower()
#         for item in option_list:
#             if item in user_response:
#                 return user_response
#         print_pause("Sorry, I don't understand.")
#
# def breakfast_bot1():
#     greeting = ["Hello, I am Bob, the Breakfast Bot.",
#                 "Today we have three breakfasts available.",
#                 "The first is waffles with strawberries and whipped cream.",
#                 "The second is sweet potato pancakes with butter and maple syrup.",
#                 "The third is nutella crepes with fresh strawberries."]
#     for item in greeting:
#         print_pause(item)
#
#     order_again = "yes"
#     while "yes" in order_again:
#         order = (valid_input("Please place your order. Would you like waffles, pancakes, or crepes?\n", ["waffles", "pancakes", "crepes"]))
#         if 'waffles' in order:
#             print_pause('Waffles it is!')
#         elif 'pancakes' in order:
#             print_pause('Pancakes it is!')
#         elif 'crepes' in order:
#             print_pause('Crepes it is!')
#
#         print_pause("Your order will be ready shortly.")
#
#         order_again = (valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n", ["yes", "no"]))
#         if 'yes' in order_again:
#             print_pause("Very good, I'm happy to take another order.")
#         elif 'no' in order_again:
#             print_pause("OK, goodbye!")
#
# breakfast_bot1()

#--------------------------------------------------------------------------

# Now, let's use functions even more to define `intro()` and `get_order()` functions to more cleanly wrap our program up. Both functions do NOT take in variables/parameters, and both functions return nothing!

# import time
#
#
# def print_pause(s):
#     print(s)
#     time.sleep(2)
#
#
# def valid_input(prompt, option_list):
#     while True:
#         user_response = input(prompt).lower()
#         for item in option_list:
#             if item in user_response:
#                 return user_response
#         print_pause("Sorry, I don't understand.")
#
#
# def intro():
#     greeting = ["Hello, I am Bob, the Breakfast Bot.",
#                 "Today we have three breakfasts available.",
#                 "The first is waffles with strawberries and whipped cream.",
#                 "The second is sweet potato pancakes with butter and maple syrup.",
#                 "The third is nutella crepes with fresh strawberries."]
#     for item in greeting:
#         print_pause(item)
#
#
# def get_order():
#     response = (valid_input("Please place your order. Would you like waffles, pancakes, or crepes?\n", ["waffles", "pancakes", "crepes"]))
#     if 'waffles' in response:
#         print_pause('Waffles it is!')
#     elif 'pancakes' in response:
#         print_pause('Pancakes it is!')
#     elif 'crepes' in response:
#         print_pause('Crepes it is!')
#     print_pause("Your order will be ready shortly.")
#
#
#
# def order_again():
#     response = (valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n", ["yes", "no"]))
#     if 'yes' in response:
#         print_pause("Very good, I'm happy to take another order.")
#         return response
#     elif 'no' in response:
#         print_pause("OK, goodbye!")
#         return response
#
#
# def breakfast_bot1():
#     intro()
#     another_order = "yes"
#     while "yes" in another_order:
#         get_order()
#         another_order = order_again()
#
#
# breakfast_bot1()

#--------------------------------------------------------------------------

# Can I simplify the remaining `breakfast_bot1()` code even further to remove the `while` loop, and call the `order_again()` function only when the user wishes to place another order? We need to include the `order_again()` function in the `get_order()` function AND we need to include the `get_order()` function within the `order_again()` function! This solution actually seems a little confusing to me, but I suppose it works in Python....

import time


def print_pause(s):
    print(s)
    time.sleep(2)


def valid_input(prompt, option_list):
    while True:
        user_response = input(prompt).lower()
        for item in option_list:
            if item in user_response:
                return user_response
        print_pause("Sorry, I don't understand.")


def intro():
    greeting = ["Hello, I am Bob, the Breakfast Bot.",
                "Today we have three breakfasts available.",
                "The first is waffles with strawberries and whipped cream.",
                "The second is sweet potato pancakes with butter and maple syrup.",
                "The third is nutella crepes with fresh strawberries."]
    for item in greeting:
        print_pause(item)


def get_order():
    response = (valid_input("Please place your order. Would you like waffles, pancakes, or crepes?\n", ["waffles", "pancakes", "crepes"]))
    if 'waffles' in response:
        print_pause('Waffles it is!')
    elif 'pancakes' in response:
        print_pause('Pancakes it is!')
    elif 'crepes' in response:
        print_pause('Crepes it is!')
    print_pause("Your order will be ready shortly.")
    order_again()



def order_again():
    response = (valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n", ["yes", "no"]))
    if 'yes' in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()
    elif 'no' in response:
        print_pause("OK, goodbye!")


def breakfast_bot():
    intro()
    get_order()


breakfast_bot()
