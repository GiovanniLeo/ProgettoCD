from dahuffman import HuffmanCodec
from FileUtils.FileUtils import FileUtils
import os
class PC:

    def PC_Encode(self, line):
        line = line.replace('\n', '')
        codec = HuffmanCodec.from_data(line)
        encoded = codec.encode(line)
        return (encoded, codec)

    def PC_Decode(self, codec, encodedString):
        decodec = codec.decode(encodedString)
        return decodec



if __name__ == '__main__':
    fileUtils = FileUtils()
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    filePathToRead = os.path.join(my_path, "..\\ProgettoCD\\OutputRLE.txt")
    fileOutputPath = os.path.join(my_path, "..\\ProgettoCD\\outputPC.txt")
    fileO = open(fileOutputPath, "wb")
    fileO.close()
    fileO = open(fileOutputPath, "ab")
    Rle_lines = fileUtils.readFileByLine(filePathToRead)
    Rle_linesLen = len(Rle_lines)

    IRle_results_arr = []
    pc = PC()
    for i in range(0, Rle_linesLen):
        encoded = pc.PC_Encode(Rle_lines[i])
        fileO.write(encoded[0])
        #print(pc.PC_Decode(encoded[1],encoded[0]))





