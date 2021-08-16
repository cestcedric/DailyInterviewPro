# O(log(n)) time: log(n) = length of n in binary
# O(log(n)) space: store binary form of n
def longest_run(n):
    binaryN = bin(n)[2:]
    
    maxSeq, currSeq = 0, 0
    for b in binaryN:
        if b == '0': currSeq = 0
        else:
            currSeq += 1
            maxSeq = max(maxSeq, currSeq)

    return maxSeq


print(longest_run(242))
# 4
