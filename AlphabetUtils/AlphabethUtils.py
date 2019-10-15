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


    '''
    Tale metodo Permuta l'alfabeto iniziale
    '''
    def appendLastCharacter(self, randomOrderedAlphabet):
        randomOrderedAlphabet.append("$")
        return randomOrderedAlphabet

    '''
    Metodo che serve a selezionare le posizioni random
    '''
    def getRandomPosition(self, alphabeth):
        maxLen = len(alphabeth)
        index = random.randint(0, maxLen)
        self.randomIndexs.append(index)
        return index

    def getRandomAlphabet(self):
        return self.randomOrderedAlphabet

    '''
    Semplica e funzione di permutazione che si occupa di 
    andare ad eseguire uno swap di variabili.
    '''
    def Perm(self, alphabet, key, r):
        alphabetLength = len(alphabet)
        for i in range(0, alphabetLength):
            s = (i + r*4 + key*2) % alphabetLength
            alphabet[i], alphabet[s] = alphabet[s], alphabet[i]

        return alphabet

    '''
    Serve per individuare l'alfabeto in un file e aggiunge dei carattere 
    speciali al fine di codificare gli spazi
    '''
    def getCharsetOfaFile(self, filePathToRead, appedLastCharacter):
        taxtInFile = open(filePathToRead, "r").read()
        charset = set(taxtInFile)
        charsList = list(charset)
        if(appedLastCharacter):
            charsList.append("ç")
            charsList.append("§")
        chars = ''.join(charsList).replace('\n', '')
        return chars

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


