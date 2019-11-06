from AlphabetUtils.AlphabethUtils import AlphabethUtils
import os

class Bmtf:

    def __init__(self, l):
        self.l = l
        self.rowtodelete = 0
        self.numofdecompression = 0

    def MtF(self, plain_text, alfabeth):
        # Initialise the list of characters (i.e. the dictionary)
        dictionary = sorted(set(alfabeth))

        # Transformation
        compressed_text = list()
        rank = 0

        # read in each character
        for c in plain_text:
            rank = dictionary.index(str(c))  # find the rank of the character in the dictionary
            compressed_text.append(str(rank))  # update the encoded text

            # update the dictionary
            dictionary.pop(rank)
            dictionary.insert(0, c)

        dictionary.sort()  # sort dictionary
        return compressed_text  # Return the encoded text as well as the dictionary

    def iMtF(self, compressed_data, alfabeth):
        compressed_text = compressed_data
        dictionary = sorted(set(alfabeth))

        plain_text = ""
        rank = 0

        # read in each character of the encoded text
        for i in compressed_text:
            # read the rank of the character from dictionary
            rank = int(i)
            plain_text += str(dictionary[rank])

            # update dictionary
            e = dictionary.pop(rank)
            dictionary.insert(0, e)

        return plain_text  # Return original string

    def cleanFile(self):
        f1 = open("filefornumblock.txt", "w")
        f1.close()
        f2 = open("fileforalfabeth.txt", "w")
        f2.close()


if __name__ == "__main__":
    alfabethutils = AlphabethUtils()
#    my_path = os.path.abspath(os.getcwd())
  #  my_path = os.path.abspath(os.path.join(my_path, '..'))
   # filePath = os.path.join(my_path, "..\\ProgettoCD\\outputSBWT.txt")
  #  alfabeth = alfabethutils.getCharsetOfaFile(filePath, False)


    test = Bmtf(4)
    test.cleanFile()
    alfabeth = 'abcdefghijklmnopqrstuvwxyz#'
    r1 = test.MtF("cavolo")
    r2 = test.MtF("rosato")
    r3 = test.MtF("banana")
    r4 = test.MtF("gigione")
    print(','.join(r4[0]))
    print(test.iMtF(r1))
    print(test.iMtF(r2))
    print(test.iMtF(r3))
    print(test.iMtF(r4))
