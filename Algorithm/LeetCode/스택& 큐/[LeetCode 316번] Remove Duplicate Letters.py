class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        duplicate_word = ''
        chars = sorted(set(s), reverse=True)
        while chars:
            suffix = s[s.index(chars[-1]):] 
            if set(s) == set(suffix): 
                s = suffix.replace(chars[-1], '')
                duplicate_word += chars[-1]
            print(s, chars[-1])
            chars.pop()
            
        return duplicate_word + s


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 집합으로정렬 
        print(s)
        for char in sorted(set(s)): 
            suffix = s[s.index(char):] 
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행 
            if set(s) == set(suffix): 
                print(char+suffix.replace(char, ''))
                return char + self.removeDuplicateLetters(suffix.replace(char, '')) 
        return ''