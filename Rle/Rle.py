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
                    encoding += str(count) +"-" + prev_char +","
                count = 1
                prev_char = char
            else:
                # Or increment our counter
                # if the characters do match
                count += 1
        else:
            # Finish off the encoding
            encoding += str(count) +"-" + prev_char +","
            return encoding[:-1]

    def rle_decode(self, data):
        decode = ''
        data = data.split(",")
        for char in data:
            # If the character is numerical...
            if char != "":
                char = char.split("-")
                decode += (char[1]+",") * int(char[0])
        #delete last element of the string
        return decode[:-1]

if __name__ == "__main__":
    rle = Rle()
    encoded_val = rle.rle_encode("1,1,13,1,1,1,0,0")
    print(encoded_val)
    print(rle.rle_decode(encoded_val))
