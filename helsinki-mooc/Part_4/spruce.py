# Write your solution here
#Attempt #2
def spruce(height: int):
    print("a spruce!")
    row = 1
    while row <= height:
        stars = 2*row -1
        spaces = height - row
        treeBranch = (" "*spaces) + ("*"*stars)
        print(treeBranch)
        row += 1
        trunkCalc = (row-1)*" " + "*"
    print(" "* (height -1) + "*")

        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)

# Attempt #1
# def spruce(height: int):
#     count = 1
#     while count < height:
#         print("*"*count)
#         count += 2
#     trunk = " " + "*" + ""
#     if count == height:
#         print(trunk)