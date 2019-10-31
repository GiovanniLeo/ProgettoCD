import Test.Compressione as cp
import Test.Decompressione as dp
import Test.cmp as cmp

#
if __name__ == '__main__':
    filename = "grammar.lsp"
    valueToPass = cp.compressione(filename)
    sbwt_dict = valueToPass[0]
    rle_dict = valueToPass[1]
    fileExtension = valueToPass[2]
    dp.decompressione(sbwt_dict, rle_dict)
    cmp.compareFile(filename, "Plain." + fileExtension)
