"""This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them."""
def get_string_distance(str1: str, str2: str):
	
    if len(str1) > len(str2):
        diff = len(str1) - len(str2)
        str1[:diff]

    elif len(str2) > len(str1):
        diff = len(str2) - len(str1)
        str2[:diff]

    else:
        diff = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1

    return diff

if __name__ == "__main__":
	print(get_string_distance("kitten", "sitting"))
	
