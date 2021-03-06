import os
import json
from FileUtils.FileUtils import FileUtils
from PC.PC import PC
from Sbwt.Sbwt import Sbwt
import time
from multiprocessing import Pool
from Bmtf.Bmtf import Bmtf
from collections import namedtuple
from Rle.Rle import Rle
import pickle
import shutil


#Immutable tupe
Row = namedtuple('Row', ['line'])

#Function used for parallelaize
def mapSbwt(x):
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePathDict = os.path.join(my_path, "..\\ProgettoCD\\Output\\dictSBWT.json")
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
        resultIsbwt = resultIsbwt.replace("ç", " ")
        resultIsbwt = resultIsbwt + '\n'
    dictFile.close()
    return resultIsbwt


if __name__ == "__main__":

    baseOutputPath = "..\\ProgettoCD\\Output\\"
    baseInputPath = "..\\ProgettoCD\\Input\\"
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    fileUtils = FileUtils()

    filePathExtension = os.path.join(my_path, baseOutputPath + "extension.txt")
    line = fileUtils.readFileByLine(filePathExtension)
    fileExtension = line[0]
    print(fileExtension)



    # Start PC
    print("Start PC")

    filePathToReadEncoded = os.path.join(my_path, baseOutputPath + "outputPC.obj")
    filePathToReadCodec = os.path.join(my_path, baseOutputPath + "outputPC_Codec.obj")
    fileOutputPath = os.path.join(my_path, baseOutputPath + "OutputPC.txt")

    fileR_ecodedArr = open(filePathToReadEncoded, 'rb')
    fileR_codecArr = open(filePathToReadCodec, 'rb')

    fileO = open(fileOutputPath, 'w')
    fileO.close()

    fileO = open(fileOutputPath, 'w')

    econdedArr = pickle.load(fileR_ecodedArr)
    codecArr = pickle.load(fileR_codecArr)

    pcUtils = PC()
    PC_start_time = time.time()

    for i in range(0, len(econdedArr)):
        decodedStr = pcUtils.PC_Decode(codecArr[i], econdedArr[i])
        fileO.write(decodedStr + "\n")

    PC_elapsed_time = time.time() - PC_start_time
    print(str(PC_elapsed_time) + " -> PC elapsedTime")

    fileO.close()

    #Start IRle
    print("Start IRLE")
    rleUtils = Rle()
    filePathToRead = os.path.join(my_path, baseOutputPath + "OutputPC.txt")
    fileOutputPath = os.path.join(my_path, baseOutputPath + "outputIRLE.txt")
    filePathDictRLE = os.path.join(my_path, baseOutputPath + "dictRLE.json")

    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)
    Rle_lines = fileUtils.readFileByLine(filePathToRead)
    Rle_linesLen = len(Rle_lines)

    with open(filePathDictRLE) as dictFile:
        RLE_Dict = json.load(dictFile)
    RLE_Dict = dict(RLE_Dict)

    IRle_results_arr = []
    IRle_start_time = time.time()
    for i in range(0, Rle_linesLen):
        Rle_lines[i] = Rle_lines[i].replace('\n', '')
        if Rle_lines[i] in RLE_Dict.keys():
            IRle_transofmedLine = rleUtils.rle_decode(RLE_Dict.get(Rle_lines[i]))
            IRle_transofmedLine = IRle_transofmedLine + '\n'
            fileO.write(IRle_transofmedLine)

    IRle_elaspsed_time = time.time() - IRle_start_time
    print(str(IRle_elaspsed_time) + " -> IRLE elapsedTime")

    fileO.close()

    #Start IBmtf
    print("Start IBMTF")
    bmtfUtils = Bmtf(6)
    filePathToRead = os.path.join(my_path, baseOutputPath + "outputIRLE.txt")
    fileOutputPath = os.path.join(my_path, baseOutputPath + "outputIBMTF.txt")
    filePathDictBMTF = os.path.join(my_path, baseOutputPath + "dictBMTF.json")
    fileO = fileUtils.openFileToWrite(fileOutputPath)
    fileO.write('')
    fileO.close()
    fileO = fileUtils.openFileToWriteAppend(fileOutputPath)
    Bmtf_lines = fileUtils.readFileByLine(filePathToRead)
    Bmtf_linesLen = len(Bmtf_lines)
    IBmtf_results_arr = []

    with open(filePathDictBMTF) as dictFile:
        BMTF_Dict = json.load(dictFile)
    BMTF_Dict = dict(BMTF_Dict)

    Ibmtf_start_time = time.time()
    for i in range(0, Bmtf_linesLen):
        Bmtf_lines[i] = Bmtf_lines[i].replace('\n', '')
        IBmtf_transofmedLine = bmtfUtils.Ibmtf(Bmtf_lines[i].split(','))
        IBmtf_transofmedLine = IBmtf_transofmedLine + '\n'
        fileO.write(IBmtf_transofmedLine)

    Ibmtf_elaspsed_time = time.time() - Ibmtf_start_time
    print(str(Ibmtf_elaspsed_time) + " -> Ibmtf elapsedTime")

    #Start Sbwt
    print("Start ISbwt")
    plainFileName = "Plain." + fileExtension
    filePathToRead = os.path.join(my_path, baseOutputPath + "outputIBMTF.txt")
    fileOutputPath = os.path.join(my_path, baseOutputPath + plainFileName)
    filePathDict = os.path.join(my_path, baseOutputPath + "dictSBWT.json")

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
        if "§" in results[i]:
            results[i] = results[i].replace("§", "$")
        fileO.write(results[i])

    fileO.close()






