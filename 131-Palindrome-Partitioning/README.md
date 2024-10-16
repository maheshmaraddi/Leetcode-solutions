Backtracking:

We use backtracking to explore all possible partitions of the string.
For each substring, we check if it's a palindrome.
If it is, we recursively check the rest of the string.
If we reach the end of the string, the current partition is valid, and we store it.

Palindrome Check:

We can check if a substring is a palindrome by comparing characters from both ends.