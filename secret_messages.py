import os
import sys
import time
import caesar
import atbash


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def hello():
    clear_screen()
    print("Welcome agent. Press any key to begin.")
    input()
    # clear screen again
    clear_screen()


def goodbye():
    clear_screen()
    # thank the user
    print("Thank you, you were never here, but see you next time.\n")
    count = 3
    while count:
        sys.stdout.write("\r")
        sys.stdout.write("This program will self destruct in {:2d} seconds...".format(count))
        sys.stdout.flush()
        time.sleep(1)
        count -= 1
    # erase all traces, this is all so secret
    clear_screen()


def program_loop():
    # available ciphers
    available_ciphers = {
        '1': 'caesar',
        '2': 'atbash'
    }

    # our program is currently running
    program_running = True
    input_char = "→ "

    while program_running:

        # print the available ciphers
        print("The available ciphers are:")

        for option, cipher in available_ciphers.items():
            print("{}: {}".format(option, cipher))

        print("Choose a cipher by entering its corresponding number below. Enter QUIT to quit.\n")

        # Collect user input
        user_input = str.lower(input(input_char))
        # -todo test user input here

        # user has entered quit
        if user_input == "quit":
            break

        # if the users choice is legit...
        if user_input in available_ciphers:
            # we have valid input,
            # we are executing a cipher
            executing_cipher = True

            clear_screen()
            selected_cipher = available_ciphers[user_input]

            while executing_cipher:

                options = {
                    "1": "encrypting",
                    "2": "decrypting"
                }
                # ask if the user is encrypting or decrypting
                print("You've selected {}, are you encrypting or decrypting?".format(str.capitalize(selected_cipher)))
                print("Enter 1 if encrypting, or 2 if decrypting. Enter BACK to return to the main menu.\n")

                encrypt_or_decrypt = str.lower(input(input_char))

                if encrypt_or_decrypt == "back":
                    break
                # if the user selection is a valid option
                elif encrypt_or_decrypt in options:

                    # okay we're good, grab the desired action as a var so we can reference it below
                    action = options[encrypt_or_decrypt]

                    # get the message form the user
                    print("Enter the text you will be {}:".format(action))
                    users_message = str.lower(input(input_char))

                    # okay, now we know which cipher, the action to take, and the message,
                    # create an instance of the cipher

                    # Caesar Cipher
                    if selected_cipher == "caesar":
                        # create an instance of caesar
                        instance = caesar.Caesar()
                    # atbash
                    elif selected_cipher == "atbash":
                        # create an instance of atbash
                        instance = atbash.Atbash()

                    # run the selected action on the created instance
                    if action == "encrypting":
                        print(instance.encrypt(users_message))
                    else:
                        print(instance.decrypt(users_message))

                    executing_cipher = False

                else:
                    print("\nError. {} is not a valid option, please try again...\n".format(encrypt_or_decrypt))

            program_running = False

        else:
            print("\nError. {} is not a valid option. Please try again.\n".format(selected_cipher))

    else:
        print("Would you like to encrypt another message? [Y,n]\n")
        if input(input_char).lower() != "n":
            program_loop()


# greet the user
hello()
# run the program
program_loop()
# we were never here
goodbye()
