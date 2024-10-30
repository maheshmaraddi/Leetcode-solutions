🔄 Anagram Checker

👋 Welcome to the Anagram Checker project! This function determines if two strings are anagrams of each other. Let’s dive into the details! 🏊‍♂️

📚 Problem Statement
Given two strings s and t, write a function to determine if t is an anagram of s.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

🛠️ Constraints
Both strings consist of lowercase English letters.

The length of both strings is in the range [1, 5 * 10^4].

🌟 Example
Example 1
Input:

s = "anagram", t = "nagaram"
Output:

true
Example 2
Input:

s = "rat", t = "car"
Output:

false
🚀 How It Works
Length Check:

If the lengths of s and t are not equal, return False.

Character Count:

Create a dictionary char_count to count the occurrences of each character in s.

For each character in s, increment its count in char_count.

Validation Against Second String:

For each character in t, decrement its count in char_count.

If any character in t is not found in char_count or its count goes below zero, return False.

Final Check:

If all values in char_count are zero, return True.