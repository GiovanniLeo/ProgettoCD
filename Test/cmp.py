import filecmp
import os

if __name__ == '__main__':
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    fileOriginal = os.path.join(my_path, "..\\ProgettoCD\\alice29.txt")
    fileDecompressed = os.path.join(my_path, "..\\ProgettoCD\\Plain.txt")

    print(filecmp.cmp(fileOriginal, fileDecompressed))
