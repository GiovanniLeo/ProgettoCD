import json
import random as random
import os
from AlphabetUtils.AlphabethUtils import AlphabethUtils
from FileUtils.FileUtils import FileUtils
from Sbwt.Sbwt import Sbwt
from Bmtf.Bmtf import Bmtf
from Rle.Rle import Rle
from PC.PC import PC
import time
import pickle
import numpy as np

if __name__ == "__main__":
    baseOutputPath = "..\\ProgettoCD\\Output\\"
    baseInputPath = "..\\ProgettoCD\\Input\\"
    fileName = "fields.c"
    fileExtension = fileName.split(".")[1]
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePathToRead = os.path.join(my_path, baseInputPath + fileName)
    alphaUtils = AlphabethUtils()
    fileUtils = FileUtils()
    sbwtUtils = Sbwt()
    transfLines = []
    transfDict = {}

    #Sto scrivendo l'estensione del file
    filePathExtension = os.path.join(my_path, baseOutputPath + "extension.txt")
    fileWextension = fileUtils.openFileToWrite(filePathExtension)
    fileWextension.write(fileExtension)
    fileWextension.close()


    #Start Sbwt
    filePath = os.path.join(my_path, baseOutputPath + "dictSBWT.json")
    fileW = fileUtils.openFileToWrite(filePath)

    fileOutputPath = os.path.join(my_path, baseOutputPath + "outputSBWT.txt")
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
        lines[i] = lines[i].replace(' ', 'ç')
        if '$' in lines[i]:
            lines[i] = lines[i].replace("$", "§")

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

    bmtfUtils = Bmtf(6)
    bmtfUtils.cleanFile()
    filePathToRead = os.path.join(my_path, baseOutputPath + "outputSBWT.txt")
    fileOutputPath = os.path.join(my_path, baseOutputPath + "outputBMTF.txt")
    filePathDict = os.path.join(my_path, baseOutputPath + "dictBMTF.json")
    fileWDict = fileUtils.openFileToWrite(filePathDict)
    fileO = open(fileOutputPath, "w")

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

    Bmtf_lines_dict = {}

    for i in range(0, len(Bmtf_transfLines)):
        line = Bmtf_transfLines[i]
        lineWOS = ''.join(line)
        lineSep = ','.join(line)
        Bmtf_lines_dict.update({lineWOS: lineSep})
        stringToWrite = lineWOS + '\n'
        fileO.write(stringToWrite)

    unglyJson = json.dumps(Bmtf_lines_dict)
    parsed = json.loads(unglyJson)
    jsonToWrite = json.dumps(parsed, indent=2, sort_keys=True)
    fileWDict.write(jsonToWrite)

    #pickle.dump(Bmtf_lines_to_write, fileO)

    #end Bmtf


    #Start RLE
    fileOutputPath = os.path.join(my_path, baseOutputPath + "outputRLE.txt")
    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)
    filePathToRead = os.path.join(my_path, baseOutputPath + "outputBMTF.txt")
    filePathDict = os.path.join(my_path, baseOutputPath + "dictBMTF.json")
    filePathDictRLE = os.path.join(my_path, baseOutputPath + "dictRLE.json")
    fileWDictRLE = fileUtils.openFileToWrite(filePathDictRLE)

    rleUtils = Rle()

    lines = fileUtils.readFileByLine(filePathToRead)
    linesLength = len(lines)

    Rle_transfLines = []


    with open(filePathDict) as dictFile:
        bmtf_Dict = json.load(dictFile)
    bmtf_Dict = dict(bmtf_Dict)

    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')

    Rle_start_time = time.time()
    for i in range(0, linesLength):
        if lines[i] in bmtf_Dict.keys():
            Rle_transfLine = rleUtils.rle_encode(bmtf_Dict.get(lines[i]))
            Rle_transfLines.append(Rle_transfLine)

    Rle_elapsed_time = time.time() - Rle_start_time
    print(str(Rle_elapsed_time) + "  -> elapsed time of  RleTrasform")

    Rle_lines_dict = {}
    for i in range(0, len(Rle_transfLines)):
        line = Rle_transfLines[i]
        lineWOS = ''.join(line.split(','))
        stringToWrite = lineWOS + '\n'
        Rle_lines_dict.update({lineWOS: line})
        fileO.write(stringToWrite)

    unglyJson = json.dumps(Rle_lines_dict)
    parsed = json.loads(unglyJson)
    jsonToWrite = json.dumps(parsed, indent=2, sort_keys=True)
    fileWDictRLE.write(jsonToWrite)

    #Start PC

    filePathToRead = os.path.join(my_path, baseOutputPath + "OutputRLE.txt")
    fileOutputPath = os.path.join(my_path, baseOutputPath + "outputPC.obj")
    fileOutputPathCodec = os.path.join(my_path, baseOutputPath + "outputPC_Codec.obj")

    fileO = open(fileOutputPath, "wb")
    fileO_Codec = open(fileOutputPathCodec, "wb")

    Rle_lines = fileUtils.readFileByLine(filePathToRead)
    Rle_linesLen = len(Rle_lines)

    pcUtils = PC()
    PC_start_time = time.time()
    encodedResult = []
    codecResult = []
    for i in range(0, Rle_linesLen):
        encoded = pcUtils.PC_Encode(Rle_lines[i])
        encodedResult.append(encoded[0])
        codecResult.append(encoded[1])

    PC_elapsed_time = time.time() - PC_start_time
    print(str(PC_elapsed_time) + "  -> elapsed time of  PCTrasform")

    pickle.dump(encodedResult, fileO)
    pickle.dump(codecResult, fileO_Codec)

    fileO.close()
    fileO_Codec.close()








