# Sangmin Lee                                           2025-05-06
# Lab: Week 15

# Description:
# If the number can divide by 3, it says "Fizz"
# If divide by 5, it says "Buzz"
# If divide by 7, it says "Bazz"
# If divide by more, it says together like "FizzBuzz"
# There are two ways to do that

def fizzBuzzModulus(n):
    result = []
    for i in range(1, n + 1):
        word = ""
        if i % 3 == 0:
            word = word + "Fizz"
        if i % 5 == 0:
            word = word + "Buzz"
        if i % 7 == 0:
            word = word + "Bazz"
        if word == "":
            word = str(i)
        result.append(word)
    return result

def fizzBuzzDict(n):
    result = []
    rule = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    for i in range(1, n + 1):
        word = ""
        for num in rule:
            if i % num == 0:
                word = word + rule[num]
        if word == "":
            word = str(i)
        result.append(word)
    return result

def main():
    n = int(input("Write your number: "))
    print("Modulus way:", fizzBuzzModulus(n))
    print("Dict way:", fizzBuzzDict(n))

if __name__ == "__main__":
    main()
