class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_map = {}

        for letter in s:
            if letter in letter_map:
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1

        even_count = 0
        isOneOdd = False
        for x in letter_map.items():
            if x[1] % 2 == 0:
                even_count += x[1]
            else:
                even_count += x[1] - 1
                isOneOdd = True
        
        if isOneOdd:
            even_count += 1
        
        return even_count


