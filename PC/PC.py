from dahuffman import HuffmanCodec
from FileUtils.FileUtils import FileUtils
import os
class PC:

    def PC_Encode(self, path):
        pass

if __name__ == '__main__':
    fileUtils = FileUtils()
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePathToRead = os.path.join(my_path, "..\\ProgettoCD\\OutputRLE.txt")
    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\outputIRLE.txt")
    fileO = open(fileOutputPath, "ab")
    Rle_lines = fileUtils.readFileByLine(filePathToRead)
    Rle_linesLen = len(Rle_lines)

    IRle_results_arr = []
    for i in range(0, Rle_linesLen):
        Rle_lines[i] = Rle_lines[i].replace('\n', '')
        codec = HuffmanCodec.from_data(Rle_lines[i])
        encoded = codec.encode(Rle_lines[i])
        fileO.write(encoded)



