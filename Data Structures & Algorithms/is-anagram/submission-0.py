class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import Counter
        letter_counter = Counter()
        for l in s:
            letter_counter[l] += 1

        for l_t in t:
            if l_t not in letter_counter.keys():
                return False

            if letter_counter[l_t] == 0:
                return False

            letter_counter[l_t] -= 1

        return True