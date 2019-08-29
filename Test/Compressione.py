import json
import random as random
import os
import sys
# lol = os.path.dirname(os.path.dirname(__file__)).replace('/', '\\') + '\\'
# sys.path.append("C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\ProgettoCD\\")
from AlphabetUtils.AlphabethUtils import AlphabethUtils
from FileUtils.FileUtils import FileUtils
from Sbwt.Sbwt import Sbwt
import time

if __name__ == "__main__":

    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePathToRead = os.path.join(my_path, "..\\ProgettoCD\\alice29.txt")
    alphaUtils = AlphabethUtils()
    fileUtils = FileUtils()
    sbwtUtils = Sbwt()
    transfLines = []
    transfDict = {}

    filePath = os.path.join(my_path, "..\\ProgettoCD\\dictSBWT.json")
    fileW = fileUtils.openFileToWrite(filePath)

    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\outputSBWT.txt")
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
