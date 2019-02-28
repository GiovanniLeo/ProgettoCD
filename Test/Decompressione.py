import json
import random as random
from AlphabetUtils.AlphabethUtils import AlphabethUtils
from FileUtils.FileUtils import FileUtils
from Sbwt.Sbwt import Sbwt
import time

if __name__ == "__main__":
    fileUtils = FileUtils()
    sbwtUtils = Sbwt()
    transfLines = []
    transfDict = {}

    filePathToRead = 'C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\outputSBWT.txt'
    filePathDict = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\dictSBWT.json"
    fileOutputPath = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Plain.txt"

    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)

    with open(filePathDict) as dictFile:
        transfDict = json.load(dictFile)

    transfDict = dict(transfDict)
    print(transfDict)
    lines = fileUtils.readFileByLine(filePathToRead)
    linesLen = len(lines)
    keysArray = [key for key in transfDict.keys()]

    for i in range(0, linesLen):
        lines[i] = lines[i].replace('\n', '')

    for i in range(0, linesLen):
        if lines[i] in transfDict.keys():
            alphabet = transfDict.get(lines[i])
            sbwtUtils.setRandomAlphabet(alphabet)
            resultIsbwt = sbwtUtils.Sibwt(lines[i])
            resultIsbwt = resultIsbwt.replace("#", " ")
            resultIsbwt = resultIsbwt + '\n'
            fileO.write(resultIsbwt)


    fileO.close()



