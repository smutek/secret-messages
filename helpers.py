import string


class Helpers():
    """
    Helper class with helpful methods
     Utility type stuff. You know.
    """

    def unique(self, text):
        """
        Returns a list of unique elements
        (Ie. this removes duplicates from a string)
        :param text: string
        :return: list
        """
        output = []

        for letter in text:
            if letter not in output:
                output.append(letter)

        return output

    def alphabet(self, type=None):
        """
        Generates an alphabet, returns either
        a string or a list
        :param type: string (default) or list
        :return: mixed
        """

        if type is None or type == "string":
            alpha = string.ascii_uppercase
        elif type == "list":
            alpha = list(string.ascii_uppercase)

        return alpha

    def polybius_square(self):
        """
        generate polybius square
        Returns a dictionary of letters (key) with their
        corresponding values per a basic polybius square
        Ie. {'A': [1, 1], 'B': [2, 1], 'C': [3, 1]...

        :return: dict
        """
        alphabet = self.alphabet()
        x = 1
        y = 1
        polybius = {}

        for letter in alphabet:
            polybius[letter] = [x, y]

            # I & J share the same key, so
            # don't increment the count on I
            if not letter == "I":
                x += 1

            # reset x when it hits 5,
            # also increment Y by 1
            if x > 5:
                x = 1
                y += 1

        return polybius
