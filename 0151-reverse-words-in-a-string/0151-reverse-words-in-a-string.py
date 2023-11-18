class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst=s.split()[::-1]
        seperator=' '
        final=seperator.join(s_lst)
        return final
        