
# 2938. Separate Black and White Balls

## Problem Statement

You are given a 0-indexed binary string `s` of length `n`, where:
- `1` represents a black ball
- `0` represents a white ball

The goal is to group all the black balls to the right and all the white balls to the left by swapping adjacent balls. 

Return the minimum number of steps required to achieve this.

## Examples

### Example 1
**Input:** 
```plaintext
s = "101"
```
**Output:** 
```plaintext
1
```
**Explanation:** 
We can group all the black balls to the right by swapping `s[0]` and `s[1]`:
- Swap: `s[0]` and `s[1]` → `s = "011"`
Thus, it takes 1 step to group the black balls.

### Example 2
**Input:** 
```plaintext
s = "100"
```
**Output:** 
```plaintext
2
```
**Explanation:** 
To group all the black balls to the right:
1. Swap `s[0]` and `s[1]` → `s = "010"`
2. Swap `s[1]` and `s[2]` → `s = "001"`

It takes a minimum of 2 steps to group the black balls.

### Example 3
**Input:** 
```plaintext
s = "0111"
```
**Output:** 
```plaintext
0
```
**Explanation:** 
All the black balls are already grouped to the right, requiring 0 steps.

## Constraints

- 1 <=n == s.length <= 10^5
- `s.length == n`
- `s[i]` is either `'0'` or `'1'`.

