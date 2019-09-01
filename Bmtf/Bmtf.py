from itertools import groupby
from AlphabetUtils.AlphabethUtils import AlphabethUtils
import os

class Bmtf:

    def __init__(self, l):
        self.l = l

    def Bmtf(self, plain_text, alfabeth, key, r):
        f = open("demofile2.txt", "a")
        alphaList = [i for i in alfabeth]
        alphaUtils = AlphabethUtils()

        input = [x for x in plain_text]  # ho convertito la stringa in una lista
        print(input)
        array = list()
        dictionary = sorted(set(alfabeth))
        compressed_text = list()
        rank = 0
        count = 0

        blocks = [input[n:n + self.l] for n in range(0, len(input), self.l)]

        for block in blocks:
                                     # sto creando una lista di liste. in array0 ho il primo blocco della lista iniziale, cioè [a,a,a].
                                     # in array1 avrò il secondo blocco della lista iniziale, cioè [b].
                                     # in array2 avrò il terzo blocco della lista iniziale, cioè [b,b].
            if count == 0:
                dictionary = alphaUtils.Perm(alphaList, key, hash(r))  # perm the block
                f.write(''.join(list(dictionary)))
                f.write("\n")

            else:
                dictionary = alphaUtils.Perm(alphaList, key, hash(("".join(array[count-1]))))  # perm the block with the precedent block permuted
                f.write(''.join(list(dictionary)))
                f.write("\n")

            for c in block:
                # per ogni carattere nel blocco applico mtf classica
                rank = dictionary.index(str(c))
                compressed_text.append(str(rank))

                dictionary.pop(rank)
                dictionary.insert(0, c)
            array.append(block)
            count = count + 1

        dictionary.sort()
        print(compressed_text)
        f.close()
        return (compressed_text, dictionary)


    def Ibmtf(self,compressed_data):
        compressed_text = compressed_data[0]
        f = open("demofile2.txt", "r")
        lines = f.readlines()
        plain_text = ""
        rank = 0
        count = 0
        numblock = 0

        # read in each character of the encoded text
        for i in compressed_text:
            if count % self.l == 0:
                dictionary = list(lines[numblock])
                numblock = numblock + 1

            # read the rank of the character from dictionary
            rank = int(i)
            plain_text += str(dictionary[rank])

            # update dictionary
            e = dictionary.pop(rank)
            dictionary.insert(0, e)
            count = count + 1

        return plain_text  # Return original string

if __name__ == "__main__":
    alfabethutils = AlphabethUtils()
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePath = os.path.join(my_path, "..\\ProgettoCD\\outputSBWT.txt")
    alfabeth = alfabethutils.getCharsetOfaFile(filePath)

    test = Bmtf(10)
    r = test.Bmtf("ANNNE'#WOAEI#LIAREU#L#TENSS###############$DRVDCD", alfabeth, 3, 2)
    print(test.Ibmtf(r))
    r = test.Bmtf("CLrrai#ol#ews#########################$l", alfabeth, 3, 2)
    print(test.Ibmtf(r))