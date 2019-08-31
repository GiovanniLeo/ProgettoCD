from collections import OrderedDict

class Rle:

    def runLengthEncoding(self, input):
    # Generate ordered dictionary of all lower
    # case alphabets, its output will be
    # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0}
        dict = OrderedDict.fromkeys(input, 0)

    # Now iterate through input string to calculate
    # frequency of each character, its output will be
    # dict = {'w':4,'a':3,'d':1,'e':1,'x':6}
        for ch in input:
            dict[ch] += 1

    # now iterate through dictionary to make
    # output string from (key,value) pairs
        output = ''
        for key, value in dict.iteritems():
            output = output + key + str(value)
        return output


# Driver function
if __name__ == "__main__":
    input = 'wwwwaaadexxxxxx'
    rle = Rle()
    print(rle.runLengthEncoding(input))