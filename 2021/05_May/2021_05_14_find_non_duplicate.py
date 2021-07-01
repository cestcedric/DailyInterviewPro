def singleNumberDic(nums):
    # O(n) time, O(n) space if nums e.g. symmetric
    dic = {}
    for n in nums:
        if n in dic: del(dic[n])
        else: dic[n] = 1
    return list(dic.keys())[0]


def singleNumberXOR(nums: list) -> int:
    # O(n) time, O(1) space
    x = 0
    for n in nums:
        x = x^n
    return x

    

print('Should be 1: {}'.format(singleNumberDic([4, 3, 2, 4, 1, 3, 2])))
print('Should be 2: {}'.format(singleNumberXOR([4, 3, 1, 4, 1, 3, 2])))
