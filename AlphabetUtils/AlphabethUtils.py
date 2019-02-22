import random

class AlphabethUtils:
    def __init__(self, alphabeth):
        self.list = list
        self.randomAlphabetDict = {}
        self.alphabeth = alphabeth
        self.alphabethDict = {}
        self.randomIndexs = []
        self.randomOrderedAlphabet = ''

    '''
    Taale metodo mappa le posiziopni delle lettere 
    nel dizionario
    '''
    def mapAlphabetToDict(self):
        alphaLen = len(self.alphabeth)

        for i in range(0, alphaLen):
            key = self.alphabeth[i]
            self.alphabethDict.update({key: i})

    # print("Alfabeto Standard")
    #print(self.alphabethDict)

    '''
    Tale metodo Permuta l'alfabeto iniziale
    '''
    def perm(self):
        self.mapAlphabetToDict()
        self.randomOrderedAlphabet = self.setRandomPosition()
        print("Alfabeto random")
        print(self.randomOrderedAlphabet)
        alphaLen = len(self.randomOrderedAlphabet)

        for i in range(0, alphaLen):
            key = self.randomOrderedAlphabet[i]
            self.randomAlphabetDict.update({key: i})
        # Mi da la chiave di indice massimo
        maxValueKey = max(self.randomAlphabetDict, key=self.randomAlphabetDict.get)
        maxValue = self.randomAlphabetDict[maxValueKey]
        lastCharacterValue = maxValue + 1
        self.randomAlphabetDict.update({"$": lastCharacterValue})
        self.randomOrderedAlphabet.append("$")
    # print("\nDizionario random")
    # print(self.randomAlphabetDict)

    '''
    Metodo che serve a selezionare le posizioni random
    '''
    def getRandomPosition(self):
        maxLen = len(self.alphabeth)
        index = random.randint(0, maxLen)
        self.randomIndexs.append(index)
        return index

    '''
    Tale metodo setta le posizioni in maniera random
    '''
    def setRandomPosition(self):
        str = sorted(self.alphabeth, key=lambda x: self.getRandomPosition())
        return str

    '''
    Metodo che permette di ordinare in maniera cutomizzata
    '''
    def customSort(self, str):
        return sorted(str, key=lambda x: self.randomAlphabetDict.get(x))

    def getRandomAlphabet(self):
        return self.randomOrderedAlphabet

    def Perm(self, alphabet, key, r):
        alphabetLength = len(alphabet)
        i = alphabetLength
        for i in range(0, alphabetLength):
            s = (i + r*4 + key*2) % alphabetLength
            alphabet[i], alphabet[s] = alphabet[s], alphabet[i]

        return alphabet

if __name__ == "__main__":
    alfabeth = 'abcdefghijklmnopqrstuvwxyz'
    list = [i for i in alfabeth]
    print(list)
    # def getRandomNumber(s):
    #     return s[0]
    # list,key = sorted(list, key=getRandomNumber)
    #
    # print(list)
    # print(key)
    prova = AlphabethUtils(alfabeth)
    # prova.perm()
    # str = 'dwe'
    # print(''.join(prova.customSort(str)))
    print(''.join(prova.Perm(list, 3, 2)))

