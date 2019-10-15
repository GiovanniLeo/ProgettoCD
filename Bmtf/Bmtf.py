import math
from itertools import groupby
from AlphabetUtils.AlphabethUtils import AlphabethUtils
import os

class Bmtf:

    def __init__(self, l):
        self.l = l
        self.rowtodelete = 0
        self.numofdecompression = 0

    def Bmtf(self, plain_text, alfabeth, key, r):
        #calcolo il numero di blocchi in cui sarà divisa la stringa
        numofblocks = (len(plain_text)//self.l)
        if len(plain_text) % self.l > 0:
            numofblocks = numofblocks + 1

        #scrivo su file il numero di blocchi usati per questa compressione
        f = open("filefornumblock.txt", "a")
        f.write(str(numofblocks))
        f.write("\n")

        f = open("fileforalfabeth.txt", "a")
        alphaList = [i for i in alfabeth]
        alphaUtils = AlphabethUtils()

        # ho convertito la stringa in una lista
        input = [x for x in plain_text]

        array = list()
        dictionary = sorted(set(alfabeth))
        compressed_text = list()
        rank = 0
        count = 0

        blocks = [input[n:n + self.l] for n in range(0, len(input), self.l)]

        for block in blocks:
                                     # sto creando una lista di liste. in array0 ho il primo blocco della lista iniziale, cioè [a,a,a].

            if count == 0:
                dictionary = alphaUtils.Perm(alphaList, key, hash(r))  # perm the first block
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

        f.close()
        return compressed_text


    def Ibmtf(self,compressed_data):

        compressed_text = compressed_data
        numofblocks = 0

        #apro il file per capire quante righe devo scartare dal file contenente tutti gli alfabeti utilizzati
        f = open("filefornumblock.txt", "r")
        fileforblock = f.readlines()
        if(self.numofdecompression != 0):
            #se non è la prima decompressione, prendo il numero di blocchi utilizzati nella compressione precedente e da questo numero inizierà il mio alfabeto
            numofblocks = fileforblock[self.numofdecompression - 1]
        self.rowtodelete = self.rowtodelete + int(numofblocks)

        #apro il file contenete tutti gli alfabeti utilizzati
        f = open("fileforalfabeth.txt", "r")
        lines = f.readlines()
        #mi prendo dalla lista gli alfabeti che servono all'attuale blocco
        lines = lines[self.rowtodelete:]

        plain_text = ""
        rank = 0
        count = 0
        indexblock = 0

        # read in each character of the encoded text
        for i in compressed_text:
            #sto passando al blocco successivo e pertanto devo prendere l'alfabeto del nuovo blocco
            if count % self.l == 0:
                dictionary = list(lines[indexblock])
                indexblock = indexblock + 1

            # read the rank of the character from dictionary
            rank = int(i)
            plain_text += str(dictionary[rank])

            # update dictionary
            e = dictionary.pop(rank)
            dictionary.insert(0, e)
            count = count + 1
            
        self.numofdecompression += 1
        f.close()
        return plain_text  # Return original string

    def cleanFile(self):
        f1 = open("filefornumblock.txt", "w")
        f1.close()
        f2 = open("fileforalfabeth.txt", "w")
        f2.close()


if __name__ == "__main__":
    alfabethutils = AlphabethUtils()
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePath = os.path.join(my_path, "..\\ProgettoCD\\outputSBWT.txt")
    alfabeth = alfabethutils.getCharsetOfaFile(filePath, False)


    test = Bmtf(4)
    test.cleanFile()

    r1 = test.Bmtf("cavolo", alfabeth, 3, 2)
    r2 = test.Bmtf("rosato", alfabeth, 3, 2)
    r3 = test.Bmtf("banana", alfabeth, 3, 2)
    r4 = test.Bmtf("gigione", alfabeth, 3, 2)
    print(','.join(r4[0]))
    print(test.Ibmtf(r1))
    print(test.Ibmtf(r2))
    print(test.Ibmtf(r3))
    print(test.Ibmtf(r4))
