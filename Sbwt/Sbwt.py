from AlphabetUtils.AlphabethUtils import AlphabethUtils

class Sbwt:

    def bwt(self, s):
        """Apply Burrows-Wheeler transform to input string."""
        assert "$" not in s, "\"$\" must be not present in the string"
        s = s + "$" # Add start and end of text marker
        table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
        last_column = [row[-1:] for row in table]  # Last characters of each row
        return "".join(last_column)  # Convert list of characters into string

    def ibwt(self, r):
        """Apply inverse Burrows-Wheeler transform."""
        table = [""] * len(r)  # Make empty table
        for i in range(len(r)):
            table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
        s = [row for row in table if row.endswith("$")][0]  # Find the correct row (ending in ETX)
        return s.strip("$")  # Get rid of start and end markers




if __name__ == "__main__":
    alfabeth = 'abcdefghijklmnopqrstuvwxyz#'
    test = Sbwt()
    #test.initialize(alfabeth, 3, 2)
    print(test.bwt("mississippi"))
    r = test.bwt("mississippi")
    # print(test.bwt("mississippi"))
    print(test.ibwt(r))
