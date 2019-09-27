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

                if prev_char == '0':
                    if count > 1:
                        encoding += str(count) +"-" + prev_char +","
                    else:
                        encoding += prev_char + ","
                count = 1
                prev_char = char
                if prev_char != '0':
                    encoding += prev_char + ","
                prev_char = char
            elif char == '0':
                # Or increment our counter
                # if the characters do match
                count += 1
            else:
                encoding += prev_char + ","
        else:
            # Finish off the encoding

            return encoding[:-1]

    def rle_decode(self, data):
        decode = ''
        data = data.split(",")
        for char in data:
            # If the character is numerical...
            if char.endswith("-0"):
                char = char.split("-")
                decode += (char[1]+",") * int(char[0])
            else:
                decode += char + ","
        #delete last element of the string
        return decode[:-1]

if __name__ == "__main__":
    rle = Rle()
    val = "2,71,28,16,3,42,1,0,0,0,0,0,12,0,0,0,0,0,12,0,0,0,0,0,12,0,0,0,0,0,12,4,44,43,37,47,8,27,30,7"
    encoded_val = rle.rle_encode(val)
    print(encoded_val + " lenght ->" + str(len(encoded_val)))
    decodedVal = rle.rle_decode(encoded_val)
    print(decodedVal + " lenht ->" + str(len(decodedVal)))
    if decodedVal == val:
        print("tranf ok")
