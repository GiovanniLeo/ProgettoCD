import os
import sys
# lol = os.path.dirname(os.path.dirname(__file__)).replace('/', '\\') + '\\'
# sys.path.append("C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\ProgettoCD\\")
import json
from FileUtils.FileUtils import FileUtils
from Sbwt.Sbwt import Sbwt
import time
from multiprocessing import Pool
from Bmtf.Bmtf import Bmtf
from collections import namedtuple

#Immutable tipe
Row = namedtuple('Row', ['line'])

#Function used for parallelaize
def mapSbwt(x):
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePathDict = os.path.join(my_path, "..\\ProgettoCD\\dictSBWT.json")
    with open(filePathDict) as dictFile:
        transfDict = json.load(dictFile)
    transfDict = dict(transfDict)

    sbwtUtils = Sbwt()
    resultIsbwt = ''

    if x.line in transfDict.keys():
        alphabet = transfDict.get(x.line)
        sbwtUtils.setRandomAlphabet(alphabet)
        lineToTransorm = x.line # line method access to
        resultIsbwt = sbwtUtils.Sibwt(lineToTransorm)
        resultIsbwt = resultIsbwt.replace("#", " ")
        resultIsbwt = resultIsbwt + '\n'
    dictFile.close()
    return resultIsbwt

def mapIbtmf(x):
    fileUtils = FileUtils()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)
    bmtfUtils = Bmtf(4)
    IBmtf_transofmedLine = bmtfUtils.Ibmtf(x.line.split(','))
    IBmtf_transofmedLine = IBmtf_transofmedLine + '\n'
    fileO.write(IBmtf_transofmedLine)
    return IBmtf_transofmedLine


if __name__ == "__main__":

    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    fileUtils = FileUtils()

    bmtfUtils = Bmtf(4)
    filePathToRead = os.path.join(my_path, "..\\ProgettoCD\\outputBMTF.txt")
    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\outputIBMTF.txt")
    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)
    Bmtf_lines = fileUtils.readFileByLine(filePathToRead)
    Bmtf_linesLen = len(Bmtf_lines)
    IBmtf_results_arr = []
    Ibmtf_start_time = time.time()
    for i in range(0, Bmtf_linesLen):
        Bmtf_lines[i] = Bmtf_lines[i].replace('\n', '')
        IBmtf_transofmedLine = bmtfUtils.Ibmtf(Bmtf_lines[i].split(','))
        IBmtf_transofmedLine = IBmtf_transofmedLine + '\n'
        fileO.write(IBmtf_transofmedLine)

    # rows = []
    # for i in range(0, Bmtf_linesLen):
    #     rows.append(Row(Bmtf_lines[i]))
    # rows = tuple(rows)


    # with Pool(1) as pool:
    #     IBmtf_results = pool.map(mapIbtmf, rows)

    # pool.close()
    # pool.join()

    Ibmtf_elaspsed_time = time.time() - Ibmtf_start_time
    print(str(Ibmtf_elaspsed_time) + " -> Ibmtf elapsedTime")

    # for i in range(0, len(IBmtf_results)):
    #     fileO.write(IBmtf_results[i])

    #Start Sbwt
    filePathToRead = os.path.join(my_path, "..\\ProgettoCD\\outputIBMTF.txt")
    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\Plain.txt")
    filePathDict = os.path.join(my_path, "..\\ProgettoCD\\dictSBWT.json")

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
          results = pool.map(mapSbwt, rows)

    pool.close()
    pool.join()
    elapsed_time = time.time() - start_time
    print(str(elapsed_time) + " -> Sbwt elapsedTime")

    results = list(results)
    for i in range(0, len(results)):
        fileO.write(results[i])

    fileO.close()
