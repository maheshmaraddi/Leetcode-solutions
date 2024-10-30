# Valid Palindrome

## Overview

This C++ implementation checks if a given string is a palindrome, ignoring non-alphanumeric characters and case differences. A palindrome reads the same forward and backward, such as "A man, a plan, a canal: Panama."

## Approach

1. **Filtering Input:**

   - The first step is to filter the input string `s` to retain only alphanumeric characters (letters and digits) and convert them to lowercase. This ensures that we can accurately compare characters without worrying about their case or any punctuation.
   - We use a loop to iterate through each character in the string. If the character is alphanumeric (checked using `isalnum()`), it is converted to lowercase (using `tolower()`) and appended to a new string called `filtered`.

2. **Two-Pointer Technique:**

   - Once we have the filtered string, we initialize two pointers: `left` starting at the beginning of the string and `right` starting at the end.
   - We enter a loop that continues as long as `left` is less than `right`. Within this loop, we check if the characters at these two pointers are equal.
   - If they are not equal, the function returns `false`, indicating that the string is not a palindrome.
   - If they are equal, we increment the `left` pointer and decrement the `right` pointer to continue checking the next pair of characters.

3. **Conclusion:**
   - If the loop completes without returning `false`, we return `true`, indicating that the filtered string is a palindrome.

## Complexity

- **Time Complexity:** O(n), where n is the length of the input string. This accounts for the initial filtering and the subsequent palindrome check.
- **Space Complexity:** O(n) for storing the filtered string.

This implementation is efficient and straightforward, making it suitable for checking whether a given string is a palindrome in a robust manner.
