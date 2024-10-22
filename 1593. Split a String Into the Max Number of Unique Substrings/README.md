# 1593. Split a String Into the Max Number of Unique Substrings

## Description

Given a string `s`, return the maximum number of unique substrings that the given string can be split into.

You can split the string `s` into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

### Examples

**Example 1:**

Input: `s = "ababccc"`  
Output: `5`  
**Explanation:**  
One way to split maximally is `['a', 'b', 'ab', 'c', 'cc']`. This way, all substrings are unique. Splitting like `['a', 'b', 'a', 'b', 'c', 'cc']` is not valid as 'a' and 'b' appear multiple times.

---

**Example 2:**

Input: `s = "aba"`  
Output: `2`  
**Explanation:**  
One way to split maximally is `['a', 'ba']`. Here, both substrings are unique. A split like `['a', 'a', 'b']` would not be valid since 'a' appears more than once.

---

**Example 3:**

Input: `s = "aa"`  
Output: `1`  
**Explanation:**  
It is impossible to split the string into more than one unique substring because both characters are 'a'. Thus, the only valid split is `['a']`.

## Constraints

- `1 ≤ s.length ≤ 16`
- `s` contains only lowercase English letters.

## Note

Make sure to explore all possible partitions and utilize a method to keep track of the unique substrings while calculating the maximum possible splits.
