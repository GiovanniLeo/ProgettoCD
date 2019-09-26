import json
import random as random
import os
import sys
# lol = os.path.dirname(os.path.dirname(__file__)).replace('/', '\\') + '\\'
# sys.path.append("C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\ProgettoCD\\")
from AlphabetUtils.AlphabethUtils import AlphabethUtils
from FileUtils.FileUtils import FileUtils
from Sbwt.Sbwt import Sbwt
from Bmtf.Bmtf import Bmtf
from Rle.Rle import Rle
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

    #Start Sbwt
    filePath = os.path.join(my_path, "..\\ProgettoCD\\dictSBWT.json")
    fileW = fileUtils.openFileToWrite(filePath)

    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\outputSBWT.txt")
    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)

    alfabeth = alphaUtils.getCharsetOfaFile(filePathToRead, True)
    lines = fileUtils.readFileByLine(filePathToRead)
    linesLength = len(lines)
    alphaLen = len(alfabeth)
    key = random.randint(0, alphaLen)

    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace(' ', '#')

    Sbwt_start_time = time.time()
    for i in range(0, linesLength):
        r = random.randint(0, alphaLen)
        randomAlphabet = sbwtUtils.initialize(alfabeth, key, r)
        transformLine = sbwtUtils.sbwt(lines[i])
        transfLines.append(transformLine)
        transfDict.update({transfLines[i]: randomAlphabet})
    Sbwt_elapsed_time = time.time() - Sbwt_start_time
    print(str(Sbwt_elapsed_time) + "  -> elapsed time of SbwtTrasform")

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
    #End Sbwt

    #Start Bmtf

    bmtfUtils = Bmtf(4)
    bmtfUtils.cleanFile()
    filePathToRead = os.path.join(my_path, "..\\ProgettoCD\\outputSBWT.txt")
    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\outputBMTF.txt")
    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)

    alfabeth = alphaUtils.getCharsetOfaFile(filePathToRead, False)
    lines = fileUtils.readFileByLine(filePathToRead)
    linesLength = len(lines)
    alphaLen = len(alfabeth)
    key = random.randint(0, alphaLen)
    Bmtf_transfLines = []

    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')

    Bmtf_start_time = time.time()
    for i in range(0, linesLength):
        r = random.randint(0, alphaLen)

        Bmtf_transformLine = bmtfUtils.Bmtf(str(lines[i]), alfabeth, key, r)
        Bmtf_transformLine = Bmtf_transformLine
        #print(transformLine)
        Bmtf_transfLines.append(Bmtf_transformLine)

    Bmtf_elapsed_time = time.time() - Bmtf_start_time
    print(str(Bmtf_elapsed_time) + "  -> elapsed time of BmtfTrasform")

    for i in range(0, len(Bmtf_transfLines)):
        line = Bmtf_transfLines[i]
        line = ','.join(line)
        stringToWrite = line + '\n'
        fileO.write(stringToWrite)

    #end Bmtf


    #Start RLE
    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\outputRLE.txt")
    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)
    filePathToRead = os.path.join(my_path, "..\\ProgettoCD\\outputBMTF.txt")
    rleUtils = Rle()

    lines = fileUtils.readFileByLine(filePathToRead)
    linesLength = len(lines)

    Rle_transfLines = []

    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')

    Rle_start_time = time.time()
    for i in range(0, linesLength):
        Rle_transfLine = rleUtils.rle_encode(lines[i])
        Rle_transfLines.append(Rle_transfLine)

    Rle_elapsed_time = time.time() - Rle_start_time
    print(str(Rle_elapsed_time) + "  -> elapsed time of  RleTrasform")

    for i in range(0, len(Rle_transfLines)):
        line = Rle_transfLines[i]
        stringToWrite = line + '\n'
        fileO.write(stringToWrite)









