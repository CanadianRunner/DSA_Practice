# Copy here code of line function from previous exercise and use it in your solution
def line(int, string):
    if string == "":
        string = "*"
        print(string[0]*int)
    else:
        print(string[0]*int)

def shape(firstInt: int, firstChar: str, secondInt: int, secondChar: str):
    firstCount = 0
    while firstCount < firstInt:
        firstCount += 1
        line(firstCount, firstChar)
    secondCount = 0
    while secondCount < secondInt:
        line(firstInt, secondChar)
        secondCount += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")