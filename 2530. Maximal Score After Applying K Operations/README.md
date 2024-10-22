# 2530. Maximal Score After Applying K Operations

## Problem Description

You are given a 0-indexed integer array `nums` and an integer `k`. You have a starting score of 0.

In one operation:
1. Choose an index `i` such that `0 <= i < nums.length`.
2. Increase your score by `nums[i]`.
3. Replace `nums[i]` with `ceil(nums[i] / 3)`.

Your task is to return the maximum possible score you can attain after applying exactly `k` operations.

## Example

### Example 1

**Input:**
```python
nums = [10, 10, 10, 10, 10]
k = 5
```
**Output:**
```
50
```
**Explanation:**
Apply the operation to each array element exactly once. The final score is `10 + 10 + 10 + 10 + 10 = 50`.

### Example 2

**Input:**
```python
nums = [1, 10, 3, 3, 3]
k = 3
```
**Output:**
```
17
```
**Explanation:**
You can do the following operations:
- Operation 1: Select `i = 1`, so `nums` becomes `[1, 4, 3, 3, 3]`. Your score increases by `10`.
- Operation 2: Select `i = 1`, so `nums` becomes `[1, 2, 3, 3, 3]`. Your score increases by `4`.
- Operation 3: Select `i = 2`, so `nums` becomes `[1, 1, 1, 3, 3]`. Your score increases by `3`.

The final score is `10 + 4 + 3 = 17`.

Constraints

    1 <= nums.length, k <= 10^5
    1 <= nums[i] <= 10^9
- `1 <= nums[i] <= 10^9`

