def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

def main():

    print(containsDuplicate([1, 2, 3, 4]))       # False
    print(containsDuplicate([1, 2, 3, 1]))       # True
    print(containsDuplicate([5, 5, 5, 5]))       # True

if __name__ == "__main__":
    main()
