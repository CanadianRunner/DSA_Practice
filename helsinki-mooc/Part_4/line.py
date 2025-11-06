# Write your solution here
def line(int, string):
    if string == "":
        string = "*"
        print(string[0]*int)
    else:
        print(string[0]*int)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
