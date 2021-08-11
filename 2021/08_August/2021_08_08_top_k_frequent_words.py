from collections import Counter, defaultdict

class Solution(object):
    # O(n * log(k)) time: with high probability, O(n * log(n)) if all words have same freq
    # O(n) space:
    # counter O(n)
    # freqToWord O(n)
    # freqValues, freqIndex O(n)
    # candidates O(n)
    def topKFrequent(self, words, k):
        # count words
        counter = Counter(words)
        freqToWord = defaultdict(list)

        # reverse lookup: frequencies to words
        for word in counter:
            freqToWord[counter[word]].append(word)

        # k top frequencies => at least k top words
        freqValues = list(freqToWord.keys())
        freqIndex = {f: i for i, f in enumerate(freqValues)}
        candidates = {}
        for _ in range(k):
            f = max(freqValues)
            if f == 0: break
            candidates[f] = freqToWord[f]
            freqValues[freqIndex[f]] = 0

        # actually find k top words
        kTopWords = []
        for f in sorted(candidates.keys(), reverse = True):
            if k <= 0: break

            tmp = sorted(candidates[f])
            kTopWords.extend(tmp[:k])

            k -= len(tmp)

        return kTopWords

        


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
