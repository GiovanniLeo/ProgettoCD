import re
class Rle:

    def rle_encode(self, data):
        encoding = ''
        prev_char = ''
        count = 1

        if not data: return ''
        data = data.split(",")
        for char in data:
            # If the prev and current characters
            # don't match...
            if char != prev_char:
                # ...then add the count and character
                # to our encoding
                if prev_char:
                    if count >= 2:
                        encoding += str(count) + "-" + prev_char + ","
                    else:
                        encoding += prev_char + ","
                count = 1
                prev_char = char
            else:
                # Or increment our counter
                # if the characters do match
                count += 1
        else:
            # Finish off the encoding
            if count >= 2:
             encoding += str(count) +"-" + prev_char +","
            else:
                encoding += prev_char + ","
            return encoding[:-1]

    def rle_decode(self, data):
        decode = ''
        data = data.split(",")
        for char in data:
            # If the character is numerical...
            if char != "":
                x = re.search("-\d+$", char)
                if x:
                    char = char.split("-")
                    decode += (char[1]+",") * int(char[0])
                else:
                    decode += char + ","
        #delete last element of the string
        return decode[:-1]

if __name__ == "__main__":
    rle = Rle()
    val = "58,22,39,11,0,21,21,21,21,54,25,48,10,13,57,60,3,39,64,0,0,41,68,21,14,3,31,14,33,29,7,66,0,0,69,2,37,0,0,0,60,0,42,43,38,0,42,6,42,1,28,13,51,31,45,70,1,1,57,46,0,16,13,3"
    encoded_val = rle.rle_encode(val)
    print(encoded_val + " lenght ->" + str(len(encoded_val)))
    decodedVal = rle.rle_decode(encoded_val)
    print(decodedVal + " lenght ->" + str(len(decodedVal)))
    if decodedVal == val:
        print("tranf ok")
