from AlphabetUtils.AlphabethUtils import AlphabethUtils



class Sbwt:

    def __init__(self):
        self.alphaUtils = AlphabethUtils()
        self.randomAlphabet = ''

    def initialize(self, alfabeth, key, r):
        alphaList = [i for i in alfabeth]
        randomOrderedAlphabet = self.alphaUtils.Perm(alphaList, key, r)
        randomOrderedAlphabet = self.alphaUtils.appendLastCharacter(randomOrderedAlphabet)
        self.randomAlphabet = ''.join(randomOrderedAlphabet)
        return self.randomAlphabet

    def setRandomAlphabet(self, alphabet):
        self.randomAlphabet = alphabet

    def sbwt(self, s):
        """Apply Burrows-Wheeler transform to input string."""
        assert "$" not in s, "Input string cannot contain STX and ETX characters"
        s = s + "$"  # Add start and end of text marker
        # Table of rotations of string (Viene ordinata secondo l'fabeto custom)
        # print(sorted(s[j:] + s[:j] for j in range(len(s))))
        matrix = sorted([s[i:] + s[:i] for i in range(len(s))], key=lambda x: [self.randomAlphabet.index(c) for c in x])
        # Table of rotations of string
        last_column = [row[-1:] for row in matrix]  # Last characters of each row
        return "".join(last_column)  # Convert list of characters into string

    def Sibwt(self, r):
        """Apply inverse Burrows-Wheeler transform."""
        table = [""] * len(r)  # Make empty table
        for i in range(len(r)):
            # Add a column of r ((Viene ordinata secondo l'fabeto custom))
            table = sorted([r[i] + table[i] for i in range(len(r))],key=lambda x: [self.randomAlphabet.index(c) for c in x])
        s = [row for row in table if row.endswith("$")][0]  # Find the correct row (ending in ETX)
        return s.strip("$")  # Get rid of start and end markers

if __name__ == "__main__":
    alfabeth = 'abcdefghijklmnopqrstuvwxyz#'
    test = Sbwt()
    test.initialize(alfabeth, 3, 2)
    print(test.sbwt("mississippi"))
    r = test.sbwt("mississippi")
    # print(test.bwt("mississippi"))
    print(test.Sibwt(r))
