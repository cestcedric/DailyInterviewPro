KAPREKAR_CONSTANT = 6174

# O(1) time: for 4-digit numbers, Kaprekar's constant is reached after <= 7 steps
# O(1) space
def num_kaprekar_iterations(n):
    if n == KAPREKAR_CONSTANT: return 0

    ascending = int(''.join(sorted(str(n))))
    descending = int(''.join(sorted(str(n), reverse = True)))
    while descending < 1000:
        descending *= 10

    return 1 + num_kaprekar_iterations(descending - ascending)


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)

print(num_kaprekar_iterations(3087))
