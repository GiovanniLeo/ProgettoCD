import random

class AlphabethUtils:
    def __init__(self):
        self.list = list
        self.randomAlphabetDict = {}
        self.alphabethDict = {}
        self.randomIndexs = []
        self.randomOrderedAlphabet = ''

    '''
    Taale metodo mappa le posiziopni delle lettere 
    nel dizionario
    '''
    def mapAlphabetToDict(self, alphabeth):
        alphaLen = len(alphabeth)

        for i in range(0, alphaLen):
            key = alphabeth[i]
            self.alphabethDict.update({key: i})

        return self.alphabethDict
    # print("Alfabeto Standard")
    #print(self.alphabethDict)

    '''
    Tale metodo Permuta l'alfabeto iniziale
    '''
    def appendLastCharacter(self, randomOrderedAlphabet):
        print("Alfabeto random")
        print(randomOrderedAlphabet)
        # alphaLen = len(randomOrderedAlphabet)
        #
        # for i in range(0, alphaLen):
        #     key = randomOrderedAlphabet[i]
        #     self.randomAlphabetDict.update({key: i})
        # # Mi da la chiave di indice massimo
        # maxValueKey = max(self.randomAlphabetDict, key=self.randomAlphabetDict.get)
        # maxValue = self.randomAlphabetDict[maxValueKey]
        # lastCharacterValue = maxValue + 1
        # self.randomAlphabetDict.update({"$": lastCharacterValue})
        randomOrderedAlphabet.append("$")
        print(randomOrderedAlphabet)
    # print("\nDizionario random")
    # print(self.randomAlphabetDict)
        return randomOrderedAlphabet

    '''
    Metodo che serve a selezionare le posizioni random
    '''
    def getRandomPosition(self, alphabeth):
        maxLen = len(alphabeth)
        index = random.randint(0, maxLen)
        self.randomIndexs.append(index)
        return index

    '''
    Tale metodo setta le posizioni in maniera random
    '''
    # def setRandomPosition(self):
    #     str = sorted(self.alphabeth, key=lambda x: self.getRandomPosition())
    #     return str

    '''
    Metodo che permette di ordinare in maniera cutomizzata
    '''
    # def customSort(self, str):
    #     return sorted(str, key=lambda x: self.randomAlphabetDict.get(x))

    def getRandomAlphabet(self):
        return self.randomOrderedAlphabet

    def Perm(self, alphabet, key, r):
        alphabetLength = len(alphabet)
        for i in range(0, alphabetLength):
            s = (i + r*4 + key*2) % alphabetLength
            alphabet[i], alphabet[s] = alphabet[s], alphabet[i]

        return alphabet

if __name__ == "__main__":
    alfabeth = 'abcdefghijklmnopqrstuvwxyz'
    list = [i for i in alfabeth]
    prova = AlphabethUtils()
    randomOrderedAlphabet = prova.Perm(list, 3, 2)
    randomOrderedAlphabet = prova.appendLastCharacter(randomOrderedAlphabet)

    # def getRandomNumber(s):
    #     return s[0]
    # list,key = sorted(list, key=getRandomNumber)
    #
    # print(list)
    # print(key)

    # prova.perm()
    # str = 'dwe'
    # print(''.join(prova.customSort(str)))


