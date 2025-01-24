class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l1 = list(word)
        if ch in l1:
            i = l1.index(ch)
            l2 = l1[0:i+1][::-1]
            l3 = l2+l1[i+1:]
            s = ''
            s1 = s.join(l3)
            return s1
        else:
            return word
