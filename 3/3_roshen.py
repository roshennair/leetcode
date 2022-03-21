# Question: 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Date: 20/03/2022
# Strategy: Sliding window technique with 2 pointers to denote the current substring
# A dictionary is used to store the indices of all the characters within the current substring
# Whenever a previously visited character is encountered, we move the start pointer to the index
# after the previous occurence of that character, and clear the dictionary of any characters
# not in the current substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If string length is 0 or 1, return string length
        if len(s) < 2:
            return len(s)

        visited_char_indices = {}
        max_length = start = 0
        end = 0

        # Iterate through characters
        for char in s:
            print('Start:', start)
            print('End:', end)
            # Check if previously visited
            if char in visited_char_indices:
                # Update max length if current length is longer
                curr_length = end - start
                if curr_length > max_length:
                    max_length = curr_length
                # Find new start index (index after previously visited character index)
                new_start = visited_char_indices[char] + 1
                # Delete all characters from dictionary that are not in current substring
                for i in range(start, new_start):
                    del visited_char_indices[s[i]]
                # Set new start index
                start = new_start
            # Add current character to dictionary and increment end pointer
            visited_char_indices[char] = end
            end += 1
            print('Visited character indices dict:', visited_char_indices)
            print(max_length)

        # If final substring is longer than max, update max length
        final_length = end - start
        if final_length > max_length:
            max_length = final_length

        return max_length

    def altLengthOfLongestSubstring(self, s: str) -> int:
        # Space complexity: O(n), n = Length of string
        # Time complexity: O(n^2)

        max_length = 0
        curr_substring = ''

        # Iterate through characters
        for char in s:
            # If character is already in substring, calculate new max length and update substring
            if char in curr_substring:
                max_length = max(max_length, len(curr_substring))
                curr_substring = curr_substring[curr_substring.index(
                    char) + 1:]
            # Add new character to substring
            curr_substring += char
            print('Current substring:', curr_substring)
            print('Max length:', max_length)

        # Update max length in case final substring is longer
        max_length = max(max_length, len(curr_substring))
        return max_length


sol = Solution()
s = "pwwkew"
print('Longest length of', s + ':', sol.lengthOfLongestSubstring(s))
