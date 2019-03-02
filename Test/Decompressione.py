import os
import sys
lol = os.path.dirname(os.path.dirname(__file__)).replace('/', '\\') + '\\'
sys.path.append("C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\ProgettoCD\\")
import json
from FileUtils.FileUtils import FileUtils
from Sbwt.Sbwt import Sbwt
import time
from multiprocessing import Pool
from collections import namedtuple


Row = namedtuple('Row', ['line'])


def prova(x):
    filePathDict = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\dictSBWT.json"
    with open(filePathDict) as dictFile:
        transfDict = json.load(dictFile)
    transfDict = dict(transfDict)

    sbwtUtils = Sbwt()
    resultIsbwt = ''

    if x.line in transfDict.keys():
        alphabet = transfDict.get(x.line)
        sbwtUtils.setRandomAlphabet(alphabet)
        lineToTransorm = x.line
        resultIsbwt = sbwtUtils.Sibwt(lineToTransorm)
        resultIsbwt = resultIsbwt.replace("#", " ")
        resultIsbwt = resultIsbwt + '\n'
    dictFile.close()
    return resultIsbwt


if __name__ == "__main__":

    fileUtils = FileUtils()
    filePathToRead = 'C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\outputSBWT.txt'
    fileOutputPath = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Plain.txt"
    filePathDict = "C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\dictSBWT.json"

    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)

    sbwtUtils = Sbwt()
    lines = fileUtils.readFileByLine(filePathToRead)
    linesLen = len(lines)

    for i in range(0, linesLen):
        lines[i] = lines[i].replace('\n', '')

    rows = []
    for i in range(0, linesLen):
        rows.append(Row(lines[i]))
    rows = tuple(rows)
   
    start_time = time.time()
    with Pool(8) as pool:
          results = pool.map(prova, rows)

    pool.close()
    pool.join()
    elapsed_time = time.time() - start_time
    print(elapsed_time)

    results = list(results)
    for i in range(0, len(results)):
        fileO.write(results[i])

    fileO.close()
