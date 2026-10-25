class Solution:
    def isPalindrome(self, s: str) -> bool:
        original_len = len(s)
        s = s.lower()
        s = ''.join([l for l in s if l.isalpha() or l.isnumeric()])

        if len(s) == 1:
            return True

        for i in range(len(s)):
            if len(s) - i - 1 < i:
                break

            if s[i] != s[len(s) - i - 1]:
                return False

        return True