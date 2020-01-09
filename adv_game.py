import time
import random


def print_pause(s):
    print(s)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        if response in options:
            return response


def intro(v, v_weapon, h, h_weapon, force_magic):
    print_pause("You are under attack from {}!".format(v))
    print_pause("""He is using his {} to cut you down and throw you into
    despair.""".format(v_weapon))
    print_pause("But you are the mighty {}!".format(h))
    print_pause("""And you cannot be defeated with your {} and some
    allies!""".format(h_weapon))
    print_pause("But you have niether at the moment.".format(h_weapon))
    print_pause("""You can either get your {}, ask one of several groups
    (Slytherins, Mandalorians, Machine Learning Engineers) to help you
    in the fight against {}, or just go out swinging with only
    {}.""".format(h_weapon, v, force_magic))


def get_weapon(v, v_weapon, h, h_weapon, force_magic, list):
    if "{}".format(h_weapon) not in list:
        print_pause("""You find your {} and are now ready to recruit
        allies!""".format(h_weapon))
        print_pause("You return to the sanctuary from whence you came!")
        list.append("{}".format(h_weapon))
    else:
        print_pause("""Oh there's your {}! You had it this whole
        time!""".format(h_weapon))
    print_pause("What do you want to do now?")
    the_game(v, v_weapon, h, h_weapon, force_magic, list)


def get_allies(v, v_weapon, h, h_weapon, force_magic, list):
    help_group = valid_input("""Which group would you like to approach? Enter
    1 for Slytherins; 2 for mandalorians; 3 for ML Engineers.\n""", ["1", "2",
                                                                     "3"])
    if "{}".format(h_weapon) not in list:
        if help_group == "1":
            print_pause("""The Slytherins laugh you off saying 'If you're {},
            then where's your {}?!'""".format(h, h_weapon))
        elif help_group == "2":
            print_pause("""The mandalorians shrug you off saying 'This guy
            claims to be {}. But I'm not seein' any {} on
            him...'""".format(h, h_weapon))
        elif help_group == "3":
            print_pause("""The Machine Learning Engineers look at you with a
            sense of disbelief and say 'With the absence of you {}, the data
            would indicate that you are not {}.'""".format(h_weapon, h))
    else:
        if help_group == "1":
            if "manda" not in list:
                print_pause("""The Slytherins look at you with contempt and
                say 'Nice {} {}, but we need to see some better odds before we
                join you!'""".format(h_weapon, h))
            elif "mle" not in list:
                print_pause("""The Slytherins look at you with contempt and
                say 'Nice {} {}, but we need to see some better odds before we
                join you!'""".format(h_weapon, h))
            elif "slyth" in list:
                print_pause("""The Slytherins are already on board! Let's do
                battle with {}""".format(v))
            elif "manda" in list and "mle" in list:
                print_pause("The Slytherins agree to join!")
                list.append("slyth")
                # break
        elif help_group == "2":
            if "manda" not in list:
                print_pause("""The Mandalorians are impressed saying 'I'll
                follow {}'s lead with his {}'.""".format(h, h_weapon))
                list.append("manda")
            else:
                print_pause("""You already recruited the Mandalorians! Find
                another group to recruit!""")
        elif help_group == "3":
            if "manda" not in list:
                print_pause("""The Machine Learning Engineers seem uneasy and
                say 'Well, we want to help, but data indicates that odds would
                be improved with more allies behind you.'""")
            elif "mle" in list:
                print_pause("""The Machine Learning Engineers have already
                agreed to donate their intellectual powers to the fight!""")
            else:
                print_pause("""The Machine Learning Engineers find the data
                before them agreeable and decide to join forces.""")
                list.append("mle")
    print_pause("What do you want to do now?")
    the_game(v, v_weapon, h, h_weapon, force_magic, list)


def go_fight(v, v_weapon, h, h_weapon, force_magic, list):
    if "{}".format(h_weapon) not in list:
        print_pause("""Without your {} and without allies, you were easily
        defeated by {}!""".format(h_weapon, v))
        print_pause("""The universe weeps as {} takes over the
        universe...""".format(v))
    elif "manda" not in list:
        print_pause("""You displayed exceptional use of {} and your
        {}.""".format(force_magic, h_weapon))
        print_pause("But without allies, {} defeated you.".format(v))
        print_pause("""The universe weeps as {} takes over the
        universe.""".format(v))
    elif "mle" not in list:
        print_pause("The Mandalorians fought valiantly.")
        print_pause("""You displayed exceptional use of {} and your
        {}.""".format(force_magic, h_weapon))
        print_pause("But {} overpowered you and the Mandalorians.".format(v))
        print_pause("""The universe weeps as {} takes over the
        universe.""".format(v))
    elif "slyth" not in list:
        print_pause("The Mandalorians fought valiantly.")
        print_pause("""You displayed exceptional use of {} and your
        {}.""".format(force_magic, h_weapon))
        print_pause("""The Machine Learning Engineers used their immense
        intellect with precision.""")
        print_pause("But alas, {} was still too much.".format(v))
        print_pause("""The universe weeps as {} takes over the
        universe.""".format(v))
    elif "slyth" in list:
        print_pause("""The Slytherins use their Magic to throw chaos into the
        battle!""")
        print_pause("""The Machine Learning Engineers use their intellect to
        destroy the enemy's communications!""")
        print_pause("""The Mandalorians use their fighting prowess to
        demoralize the enemy!""")
        print_pause("""You have your epic battle against {} and defeat
        him!""".format(v))
        print_pause("The universe rejoices your courage and skill!")
    play_again()


def the_game(v, v_weapon, h, h_weapon, force_magic, list):
    response = valid_input("""Enter 1 to get your {}; 2 to ask for help from
    the groups; 3 to dive into the fight.\n""".format(h_weapon), ["1", "2",
                                                                  "3"])
    if response == "1":
        get_weapon(v, v_weapon, h, h_weapon, force_magic, list)
    elif response == "2":
        get_allies(v, v_weapon, h, h_weapon, force_magic, list)
    elif response == "3":
        go_fight(v, v_weapon, h, h_weapon, force_magic, list)


def play_again():
    again = valid_input("""Would you like to play again? Enter y/n:\n""",
                        ["y", "n"])
    if again == "y":
        game_play()
    else:
        print_pause("Thanks for playing! See you next time!")


def game_play():
    item_list = []

    villians = ["Kylo Ren", "Darth Vader", "Emperor Palpatine", "Voldemort",
                "Donald Trump"]
    heroes = ["Yoda", "Obi-Wan Kenobi", "Harry Potter", "Albus Dumbledore"]

    v = random.choice(villians)
    if v in ["Kylo Ren", "Darth Vader", "Emperor Palpatine"]:
        v_weapon = "Lightsaber"
        force_magic = "The Force"
    elif v == "Voldemort":
        v_weapon = "Wand"
        force_magic = "Magic"
    elif v == "Donald Trump":
        v_weapon = "Twitter"
        force_magic = "Irrationality"

    h = random.choice(heroes)
    if h in ["Yoda", "Obi-Wan Kenobi"]:
        h_weapon = "Lighsaber"
        force_magic = "The Force"
    else:
        h_weapon = "Wand"
        force_magic = "Magic"

    intro(v, v_weapon, h, h_weapon, force_magic)
    the_game(v, v_weapon, h, h_weapon, force_magic, item_list)


game_play()
