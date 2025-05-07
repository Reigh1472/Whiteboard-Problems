# Sangmin Lee                                           2025-05-06
# Lab: Week 15

# Description:
# This program takes a word and shows the reversed version.
# One way uses loop. Another way uses function that calls itself

def reverseIterative(s):
    reversed_word = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_word = reversed_word + s[i]
    return reversed_word

def reverseRecursive(s):
    if len(s) <= 1:
        return s
    return reverseRecursive(s[1:]) + s[0]

def main():
    word = input("Type a word to reverse: ")
    print("Reversed (loop):", reverseIterative(word))
    print("Reversed (recursion):", reverseRecursive(word))

if __name__ == "__main__":
    main()
