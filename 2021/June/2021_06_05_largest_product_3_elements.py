# O(n) time complexity, one iteration through lst to find min and max values
# O(1) space complexity, only need space for 5 extra variables
def maximum_product_of_three(lst):
    # -n * -n = +n^2 => very small values multiplied can also be big
    min1 = min2 = 1001
    max1 = max2 = max3 = -1001
    for n in lst:
        if n <= min1: min2, min1 = min1, n
        elif n < min2: min2 = n
        if n >= max1: max3, max2, max1 = max2, max1, n
        elif n >= max2: max3, max2 = max2, n
        elif n > max3: max3 = n

    return max(min1 * min2 * max1, max1 * max2 * max3)


print('Should be 128: {}'.format(maximum_product_of_three([-4, -4, 2, 8])))
print('Should be 6: {}'.format(maximum_product_of_three([1, 2, 3])))