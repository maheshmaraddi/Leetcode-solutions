## 31. Next Permutation 

### Solution Performance
- **Runtime**: 4 ms  
  Beats 92.57% of submissions

- **Memory Usage**: 11.69 MB  
  Beats 32.51% of submissions

### Problem
Given an array `arr[]` of integers, rearrange its elements into the **lexicographically next greater permutation**. If such a permutation is not possible, rearrange it to the lowest possible order (i.e., sorted in ascending order).

### Example:
Input: nums = [1, 2, 3]  
Output: [1, 3, 2]

## Algorithm

1. **Find the Break-Point**:  
   Starting from the end, find the first index where an element is smaller than the one after it. This index is the break-point.

2. **No Break-Point**:  
   If the array is entirely in descending order, it's the last permutation. Simply reverse the array to get the first permutation (sorted in ascending order).

3. **If a Break-Point Exists**:  
   Find the smallest element larger than the break-point element (from the right side of the array), swap them, and reverse the part of the array after the break-point.

   This gives the next lexicographical permutation.

## Time Complexity

- **O(3N)**  
  `N` is the size of the array.  
  - Finding the break-point: O(N)  
  - Finding the next greater element: O(N)  
  - Reversing the array: O(N)  
  This sums up to O(3N), but it's typically simplified to O(N).

## Space Complexity

- **O(1)**  