# Single Number

## Overview

This C++ implementation solves the problem of finding the single number in an array where every element appears twice except for one. The algorithm utilizes the properties of the XOR bitwise operation to efficiently identify the unique number.

## Problem Statement

Given an integer array `nums` where each element appears twice except for one, find and return the single number that does not appear twice. You must implement a solution with a linear runtime complexity and use constant extra space.

## Approach

### Using XOR Operation

1. **XOR Properties**:

   - The XOR operation (`^`) has some important properties:
     - \( a \oplus a = 0 \): Any number XORed with itself results in 0.
     - \( a \oplus 0 = a \): Any number XORed with 0 results in the number itself.
     - XOR is commutative and associative, meaning the order of operations does not matter.

2. **Iterating through the Array**:

   - Initialize a variable `ans` to 0. This variable will hold the result of the XOR operations.
   - Iterate through each element in the input vector `nums`. For each element `x`, perform the XOR operation with `ans`: `ans ^= x`.
   - Due to the properties of XOR, all numbers that appear twice will cancel each other out (resulting in 0), and the remaining value in `ans` will be the single number.

3. **Return the Result**:
   - After processing all elements in the array, `ans` will contain the single number that does not appear twice.

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of elements in the input array. This is because we traverse the array once.
- **Space Complexity**: O(1), as we are using only a constant amount of space for the variable `ans`, regardless of the input size.

## Conclusion

This solution effectively identifies the single number in an array with a time-efficient and space-efficient approach, leveraging the unique properties of the XOR operation. This makes it suitable for large datasets where minimizing time and space complexity is critical.
