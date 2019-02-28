import json
import random as random
from AlphabetUtils.AlphabethUtils import AlphabethUtils
from FileUtils.FileUtils import FileUtils
from Sbwt.Sbwt import Sbwt
import time

if __name__ == "__main__":

    filePathToRead = 'C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Prova.txt'
    alphaUtils = AlphabethUtils()
    fileUtils = FileUtils()
    sbwtUtils = Sbwt()
    transfLines = []
    transfDict = {}

    filePath = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\dictSBWT.json"
    fileW = fileUtils.openFileToWrite(filePath)

    fileOutputPath = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\outputSBWT.txt"
    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)

    alfabeth = alphaUtils.getCharsetOfaFile(filePathToRead)
    lines = fileUtils.readFileByLine(filePathToRead)
    linesLength = len(lines)
    alphaLen = len(alfabeth)
    key = random.randint(0, alphaLen)

    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace(' ', '#')

    start_time = time.time()
    for i in range(0, linesLength):
        r = random.randint(0, alphaLen)
        randomAlphabet = sbwtUtils.initialize(alfabeth, key, r)
        transformLine = sbwtUtils.sbwt(lines[i])
        transfLines.append(transformLine)
        transfDict.update({transfLines[i]: randomAlphabet})
    elapsed_time = time.time() - start_time
    print(elapsed_time)

    # print(transfLines)
    for i in range(0, len(transfLines)):
        stringToWrite = transfLines[i] + '\n'
        fileO.write(stringToWrite)

    unglyJson = json.dumps(transfDict)
    parsed = json.loads(unglyJson)
    jsonToWrite = json.dumps(parsed, indent=2, sort_keys=True)
    fileW.write(jsonToWrite)
    fileW.close()
    fileO.close()
