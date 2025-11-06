# Write your solution here

def longest(strings: list):
    i = 0
    longestWord = []

    for word in strings:
        if len(word) >= len(longestWord):
            longestWord = word
        i += 1
    return longestWord



if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
