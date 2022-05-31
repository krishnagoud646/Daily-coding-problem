"""This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character. For example, 
the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A"."""
class RunLengthEncoding:
    @staticmethod #cannot access the instance of class.
    def encode(string):
        string = list(string)
        char = string.pop(0)
        times = 1
        encoding = ""
        while string:
            this_char = string.pop(0)
            if this_char==char:
                times += 1
            else:
                encoding += "{0}{1}".format(times, char)
                times = 1
            char = this_char
        encoding += "{0}{1}".format(times, char)
        return encoding


if __name__=='__main__':
    rle = RunLengthEncoding()
    string = "AAAABBBCCDAA"
    encoded = rle.encode(string)
    print("The Encoded String is:",encoded)
