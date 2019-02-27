from AlphabetUtils.AlphabethUtils import AlphabethUtils as alphaUtils
from Sbwt.Sbwt import Sbwt
from FileUtils.FileUtils import FileUtils
import random as random
import json

if __name__ == "__main__":
    filePathToRead = 'C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Prova.txt'
    # ---------- Serve per individuare l'alfabeto in un file ----------
    taxtInFile = open(filePathToRead, "r").read()
    charset = set(taxtInFile)
    charsList = list(charset)
    charsList.append("#")
    chars = ''.join(charsList).replace('\n', '')
    # ---------- Serve per individuare l'alfabeto in un file ----------
    alfabeth = chars
    fileUtils = FileUtils()
    lines = fileUtils.readFileByLine("C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Prova.txt")
    linesLength = len(lines)
    alphaLen = len(alfabeth)
    key = random.randint(0, alphaLen)
    sbwtUtils = Sbwt()
    transfLines = []
    transfDict = {}
    filePath = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\dictSBWT.txt"
    fileW = fileUtils.openFileToWrite(filePath)
    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace(' ', '#')
        lines[i] = lines[i].lower()


    for i in range(0, linesLength):
        r = random.randint(0, alphaLen)
        randomAlphabet = sbwtUtils.initialize(alfabeth, key, r)
        transformLine = sbwtUtils.sbwt(lines[i])
        transfLines.append(transformLine)
        transfDict.update({transfLines[i]: randomAlphabet})

    print(transfLines)
    fileW.write(json.dumps(transfDict))
    fileW.close()






