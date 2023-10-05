# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:				
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# use Counter and compare
# count each and check if count is less or equal

# check each letter and compare to mag

# check for each letter than is not in magazine
# 
from collections import Counter
# counter is a sub class of dict... so it will work the same way
def solution(ransomeNote, magazine):
    note = Counter(ransomeNote)
    mag = Counter(magazine)
    res = True
    for char, val in note.items():
        if not mag.get(char, 0) >= note[char]:
            res = False
    return res


#     # for 
#     name = "apple"
#     name.replace('c', '', 1)
    

# solution("happy times", "pay me")