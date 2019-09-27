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
                        encoding += str(count) +"-" + prev_char +","
                    else:
                        encoding += prev_char + ","
                count = 1
                # if prev_char != '0':
                #     encoding += prev_char + ","
                prev_char = char
            elif char:
                # Or increment our counter
                # if the characters do match
                count += 1
            else:
                encoding += prev_char + ","
        else:
            # Finish off the encoding
            encoding += prev_char
            return encoding

    def rle_decode(self, data):
        decode = ''
        data = data.split(",")
        for char in data:
            splittedChar = char.split("-")
            # If the character is numerical...
            if splittedChar and len(splittedChar) > 1:
                decode += (splittedChar[1]+",") * int(splittedChar[0])
            else:
                decode += char + ","
        #delete last element of the string
        return decode[:-1]

if __name__ == "__main__":
    rle = Rle()
    val = "16,32,51,71,2,7,1,2,1,0,0,0,4,0,0,0,0,0,18,0,0,0,0,0,18,0,0,0,0,0,18,0,0,0,0,7,39"
    encoded_val = rle.rle_encode(val)
    print(encoded_val + " lenght ->" + str(len(encoded_val)))
    decodedVal = rle.rle_decode(encoded_val)
    print(decodedVal + " lenght ->" + str(len(decodedVal)))
    if decodedVal == val:
        print("tranf ok")
