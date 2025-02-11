class Solution:
    """ Class to merge strings alternately"""

    def MergeWords(self, word1: str, word2: str) -> str:
        """Method to merge words alternately
        """
        merged = []
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1
        return "".join(merged)

# Test our solutions
solution = Solution()
print("Test1: ", solution.MergeWords("abc", "pqr"))
print("Test2: ", solution.MergeWords("ab", "pqrs"))
print("Test3: ", solution.MergeWords("abcd", "pq"))
