import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def program_loop():

    # available ciphers
    available_ciphers = [
        'caesar',
        'atbash'
    ]

    # our program is currently running
    program_running = True

    while program_running:

        clear_screen()

        print("The available ciphers are:")

        for cipher in available_ciphers:
            print("- {}".format(str.capitalize(cipher)))

        print("Choose a cipher by entering its name below,\n"
              "or enter QUIT to quit.")

        user_input = input("=> ")
        selected_cipher = str.lower(user_input)

        # user has entered quit
        if selected_cipher == "quit":
            print("Thank you, see you next time.")
            break

        if selected_cipher in available_ciphers:
            # we have valid input, move on
            executing_cipher = True
            clear_screen()
            while executing_cipher:

                print("You've selected {}, are you encrypting or decrypting?\n"
                      "Enter 1 if encrypting, or 2 if decrypting. Enter QUIT to quit.".format(selected_cipher))

                encrypt_or_decrypt = str.lower(input())

                if encrypt_or_decrypt == "quit":
                    print("Thank you, see you next time.")
                    break

                if encrypt_or_decrypt == "1":
                    print("Encrypting....")
                    executing_cipher = False
                elif encrypt_or_decrypt == "2":
                    print("Decrypting")
                    executing_cipher = False
                else:
                    print("Error, {} is not a valid option, please try again...".format(encrypt_or_decrypt))

            program_running = False
        else:
            print("Error. Sorry, {} is not a valid entry. Please double check and try again.".format(selected_cipher))

    else:
        if input("Would you like to encrypt another message? [Y, n]").lower() != "n":
            program_loop()


clear_screen()
print("Welcome to the secret message machine.\n")
input("Press any key to begin.")
clear_screen()
program_loop()
print("Thank you, see you next time.")
