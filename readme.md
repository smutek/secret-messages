# Secret Messages

Project 2 in the Treehouse Python tech degree program.

## Project Overview

Most of us have, at one time or another, wanted to pass messages to our friends that other people couldn't read. Maybe it was a note in class, a midnight rendezvous, or something more serious like invasion plans. Whatever the purpose, you'd want your message to be encoded so only the people you want to can read it. That's where ciphers come in!

Ciphers are repeatable ways to encode a message. One of the most famous is the Caesar Cipher, used by Julius Caesar for his private communications. He would take each letter of the message and change it to the letter that was three characters further on in the Roman alphabet. For example, if I was going to encode the word "dog", using the American English alphabet, I would change the "d" to "g", which is three letters further on. The "o" would become "r", and the "g" turns into "j". Instead of sending "dog" to my friend, I'd send "grj". To figure it out, my friend would move each letter back three characters.

One thing Julius Caesar didn't have, though, is a computer to do all of this encoding and decoding for him!

Your job is to take a few of the famous ciphers listed here and implement them in Python so you can quickly encode and decode secret messages. Each cipher should be created as a Python class and each has to expose two methods: encrypt and decrypt. Each of these methods should take a single string to be encoded or decoded and should return the properly encoded or decoded version of the string according to the cipher.

Some of these ciphers might require other attributes to be set, but I'll leave that up to you to decide.

__NOTE: The included sample Caesar Cipher does not count towards one of the three required implementations.__

## Instructions

1. Choose at least three basic ciphers from the following list to implement encrypting and decrypting abilities.
    - [Alberti cipher](https://en.wikipedia.org/wiki/Alberti_cipher)
    - [Affine cipher](https://en.wikipedia.org/wiki/Affine_cipher)
    - [Atbash cipher](https://en.wikipedia.org/wiki/Atbash)
    - [Polybius square cipher](https://en.wikipedia.org/wiki/Polybius_square)
    - [Transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher)
    - [ADFGVX cipher](https://en.wikipedia.org/wiki/ADFGVX_cipher)
    - [Bifid cipher](https://en.wikipedia.org/wiki/Bifid_cipher)
    - [Keyword cipher](https://en.wikipedia.org/wiki/Keyword_cipher)
    - [Hill cipher](https://en.wikipedia.org/wiki/Hill_cipher)
    
2. Provide a command line menu providing an option to either encrypt or decrypt a value and then a sub menu with a list of implemented ciphers.
3. Write a separate class, which inherits from cipher, and implements encrypt and decrypt functionality for each of your chosen ciphers.
4. Prompt the user for input to encrypt or decrypt and, if applicable, any additional input settings required to perform the cipher process.
5. The input value is correctly encrypted or decrypted using the chosen cipher and the output is displayed on the screen.
6. Remember to include informative docstrings in your functions and/or methods.
7. Make sure to follow the PEP 8 guidelines for coding style and write organized, easy to follow code. General code comments are great to add to your code too.

### Extra Credit
To get an "exceeds" rating, you can expand on the project in the following ways:

1. Implement a one time pad to secure the cipher. A one time pad is an additional input step required prior to encrypting and decrypting a message. As long as both the sender and receiver use the same pad, the message itself becomes secure. Without the pad, the message cannot be recovered.
2. Encrypted output is displayed in 5 character blocks, with padding added as required. For example if the message to encrypt is “The quick brown fox.” The output would be represented as something like `LFDKA NMYML K1KZE &XPQR`.