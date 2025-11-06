# Copy here code of line function from previous exercise
def line(int, string):
    if string == "":
        string = "*"
        print(string[0]*int)
    else:
        print(string[0]*int)

def triangle(size):
    width = 0
    while width < size:
        width += 1
        line(width, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
