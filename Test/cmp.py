import os

def textCompare(fl1,fl2):
    file1 = open(fl1, 'r')
    file2 = open(fl2, 'r')
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    file1.close()
    file2.close()
    if lines1 == lines2:
        return True
    else:
        return False
def compareFile(originFile, decopressedFile):
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    fileOriginal = os.path.join(my_path, "..\\ProgettoCD\\Input\\" + originFile )
    fileDecompressed = os.path.join(my_path, "..\\ProgettoCD\\Output\\" + decopressedFile)
    outputPath =  os.path.join(my_path, "..\\ProgettoCD\\Output\\")
    onlyfiles = [f for f in os.listdir(outputPath) if os.path.isfile(os.path.join(outputPath, f))]

    for i in range(0, len(onlyfiles)):
        if onlyfiles[i] != decopressedFile:
            filePath = os.path.join(my_path, "..\\ProgettoCD\\Output\\"+ onlyfiles[i] )
            os.remove(filePath)
    print("-----------------------------------------------------------------------")
    print("Lossless compression ->" + str(textCompare(fileOriginal, fileDecompressed)))
