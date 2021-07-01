class Solution(object):
    def pushDominoes(self, dominoes):
        # O(n^2) time complexity, iterate over whole string as long as dominoes can fall
        # O(n) time complexity if we assume that only one step has to be computed
        # O(n) space complexity, one list created with same size as dominoes
        pressure = 'R' in dominoes or 'L' in dominoes
        length = len(dominoes)
        if length < 2: return dominoes
        while pressure:
            tmp = list(dominoes)
            pressure = False
            if dominoes[0] == '.' and dominoes[1] == 'L': tmp[0] = 'L'
            for i in range(1, length - 1):
                if dominoes[i] == '.':
                    right =  dominoes[i-1] == 'R'
                    left = dominoes[i+1] == 'L'
                    if left != right: 
                        tmp[i] = 'R' if right else 'L'
                        pressure = True
            if dominoes[length-1] == '.' and dominoes[length-2] == 'R': tmp[length-1] = 'R'
            dominoes = ''.join(tmp)
        return dominoes


print('Should be \'..RR.LL..RR\': {}'.format(Solution().pushDominoes('..R...L..R.')))
print('Should be \'RR.L\': {}'.format(Solution().pushDominoes('RR.L')))
print('Should be \'....\': {}'.format(Solution().pushDominoes('....')))
