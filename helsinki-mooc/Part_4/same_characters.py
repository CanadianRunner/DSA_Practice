# Write your solution here
def same_chars(char: str, integer1: int, integer2: int):
    charLength = len(char)
    if not (0 <=integer1 < charLength and 0 <= integer2 < charLength):
        return False
    if char[integer1] == char[integer2]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))