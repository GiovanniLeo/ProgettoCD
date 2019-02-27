
class FileUtils:

    def __init__(self):
        pass

    def openFileToWrite(self, path):
        fileToWrite = open(path, "w")
        return fileToWrite

    def openFileToWriteAppend(self, path):
        fileToWrite = open(path, "a")
        return fileToWrite

    def readFileByLine(self, path):
        lines = open(path, "r").readlines()
        return lines

    def writeInFile(self, fileToWrite, elemntsToWrite):
        fileToWrite.write(elemntsToWrite)

    def writeInFileAppend(self, fileToWrite, elemnt):
        fileToWrite.write(elemnt)


if __name__ == "__main__":
    fileUtils = FileUtils()
    lines = fileUtils.readFileByLine("C:\\Users\\johnn\\Desktop\\Unisa\\Magistrale\\CD\\ProgettoCD\\Prova.txt")
    linesLength = len(lines)

    for i in range(0, linesLength):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace(' ', '#')

    print(lines)