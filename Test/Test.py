from AlphabetUtils.AlphabethUtils import AlphabethUtils
from Sbwt.Sbwt import Sbwt
from FileUtils.FileUtils import FileUtils
import random as random
import json

if __name__ == "__main__":
    filePathToRead = 'C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Prova.txt'
    alphaUtils = AlphabethUtils()
    fileUtils = FileUtils()
    sbwtUtils = Sbwt()
    transfLines = []
    transfDict = {}

    filePath = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\dictSBWT.txt"
    fileW = fileUtils.openFileToWrite(filePath)

    fileOutputPath = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\outputSBWT.txt"
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)

    alfabeth = alphaUtils.getCharsetOfaFile(filePathToRead)
    lines = fileUtils.readFileByLine("C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Prova.txt")
    linesLength = len(lines)
    alphaLen = len(alfabeth)
    key = random.randint(0, alphaLen)



    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace(' ', '#')

    for i in range(0, linesLength):
        r = random.randint(0, alphaLen)
        randomAlphabet = sbwtUtils.initialize(alfabeth, key, r)
        transformLine = sbwtUtils.sbwt(lines[i])
        transfLines.append(transformLine)
        transfDict.update({transfLines[i]: randomAlphabet})

    print(transfLines)
    for i in range(0, len(transfLines)):
        stringToWrite = transfLines[i] + '\n'
        fileO.write(stringToWrite)

    fileW.write(json.dumps(transfDict))
    fileW.close()
    fileO.close()
