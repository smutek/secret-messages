import os
import sys
import time


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
    available_ciphers = [
        'caesar',
        'atbash'
    ]

    # our program is currently running
    program_running = True
    input_char = "→ "

    while program_running:

        print("The available ciphers are:")

        count = 1
        for cipher in available_ciphers:
            print(str(count) + ". {}".format(str.capitalize(cipher)))
            count += 1

        print("Choose a cipher by entering its corresponding number below. Enter QUIT to quit.\n")

        user_input = input(input_char)
        # -todo test user input here
        selected_cipher = available_ciphers[int(user_input) - 1]

        # user has entered quit
        if selected_cipher == "quit":
            break

        if selected_cipher in available_ciphers:
            # we have valid input, move on
            executing_cipher = True
            clear_screen()
            while executing_cipher:

                print("You've selected {}, are you encrypting or decrypting?".format(str.capitalize(selected_cipher)))
                print("Enter 1 if encrypting, or 2 if decrypting. Enter BACK to return to the main menu.\n")

                user_input = input(input_char)
                encrypt_or_decrypt = str.lower(user_input)

                if encrypt_or_decrypt == "back":
                    break

                if encrypt_or_decrypt == "1":
                    print("Encrypting....")
                    executing_cipher = False
                elif encrypt_or_decrypt == "2":
                    print("Decrypting")
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

