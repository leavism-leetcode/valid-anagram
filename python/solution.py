# Copy/paste template from LeetCode below
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        
        for letter in t:
            s_dict[letter] = s_dict.get(letter, 0) - 1
        
        for count in s_dict.values():
            if count != 0:
                return False
        
        return True

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
solution = Solution()

result = solution.isAnagram("anagram", "nagaram")

print(result)


