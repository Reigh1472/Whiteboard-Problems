# Sangmin Lee                                           2025-05-06
# Lab: Week 15

# Description:
# This checks if the word I type is the same forward and backward
# One way uses loop, and the other uses recursion (call itself)
# If the word is same, it shows True. If not, it shows False


def isPalindromeIterative(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeRecursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursive(s[1:-1])

def main():
    word = input("Type a word to check: ")
    print("Iterative check:", isPalindromeIterative(word))
    print("Recursive check:", isPalindromeRecursive(word))

if __name__ == "__main__":
    main()
