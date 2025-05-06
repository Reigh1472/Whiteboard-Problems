def topKFrequent(nums, k):
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

def main():
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(topKFrequent([1], 1))                # [1]
    print(topKFrequent([4, 1, 2, 2, 3, 3, 3], 2))  # [3, 2]

if __name__ == "__main__":
    main()
