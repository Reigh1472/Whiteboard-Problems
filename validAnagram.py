def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

def main():
    print(isAnagram("anagram", "nagaram"))  # True
    print(isAnagram("rat", "car"))          # False
    print(isAnagram("listen", "silent"))    # True

if __name__ == "__main__":
    main()
