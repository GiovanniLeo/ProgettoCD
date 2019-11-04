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
if __name__ == '__main__':
    my_path = os.path.abspath(os.getcwd())
    my_path = os.path.abspath(os.path.join(my_path, '..'))
    fileOriginal = os.path.join(my_path, "..\\ProgettoCD\\Input\\fields.c")
    fileDecompressed = os.path.join(my_path, "..\\ProgettoCD\\Output\\Plain.c")
    print(textCompare(fileOriginal, fileDecompressed))
