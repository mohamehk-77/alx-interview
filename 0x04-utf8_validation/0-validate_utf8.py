#!/usr/bin/python3
def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0


# Testing the function with provided test cases
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
