# 1071. Greatest Common Divisor of Strings
# Easy
# 4.3K
# 892
# Companies
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         def isDivisor(substr, string):
#             # empty substr is the divisor of any string
#             if not substr:
#                 return True

#             if len(substr) <= len(string) and string.startswith(substr):
#                 remainingStr = string[len(substr) :]
#                 if remainingStr:
#                     return isDivisor(substr, remainingStr)
#                 else:
#                     return True
#             else:
#                 return False

#         # find minimum common divisor for both
#         def minComDiv(str1, str2):
#             # start with first letter,
#             index = 0
#             subStr = ""
#             minStr = str1 if len(str1) <= len(str2) else str2
#             while index < len(minStr):
#                 subStr += minStr[index]
#                 if isDivisor(subStr, str1) and isDivisor(subStr, str2):
#                     return subStr
#                 else:
#                     index += 1

#             if subStr == minStr:
#                 return ""

#         # max common divisor is the multipler of minimum common divisor
#         minCD = minComDiv(str1, str2)
#         maxCD = minCD
#         while len(maxCD) <= len(str1) and len(maxCD) <= len(str2):
#             if maxCD and isDivisor(maxCD, str1) and isDivisor(maxCD, str2):
#                 # maxCD *= 2
#                 maxCD += minCD
#             else:
#                 # maxCD = maxCD[: int(len(maxCD) / 2)]
#                 maxCD = maxCD[: -len(minCD)]
#                 return maxCD

#         # return maxCD[: int(len(maxCD) / 2)]

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        gcdLen = gcd(len1, len2)
        gcdStr = str1[:gcdLen]

        if str1 == gcdStr * (len1 // gcdLen) and str2 == gcdStr * (len2 // gcdLen):
            return gcdStr
        else:
            return ""


# str1 = "AAAAAAAAA"
str1 = "ABCABC"
str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

# str2 = "AAACCC"
str2 = "ABC"
str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
print(Solution().gcdOfStrings(str1, str2))
