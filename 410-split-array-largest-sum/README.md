<h2><a href="https://leetcode.com/problems/split-array-largest-sum/">Split Array Largest Sum</a></h2>  
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. The goal is to split <code>nums</code> into <code>k</code> non-empty subarrays such that the largest sum of any subarray is minimized.</p>

<p><strong>Note:</strong> A subarray is a contiguous part of the array.</p>

<p>&nbsp;</p> 

### Explanation:

- **Array**: The array <code>nums[i]</code> represents the elements of the integer array.
- **Subarray**: A subarray is a contiguous segment of the array.
- **Goal**: Minimize the largest sum among all subarrays formed by splitting the array into at most <code>k</code> parts.

---

### <strong class="example">Example 1:</strong>

<pre>
<strong>Input:</strong> nums = [7,2,5,10,8], k = 2
<strong>Output:</strong> 18
<strong>Explanation:</strong> 
- The optimal way to split the array is into [7,2,5] and [10,8], where the largest sum is 18.
</pre>

### <strong class="example">Example 2:</strong>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], k = 2
<strong>Output:</strong> 9
<strong>Explanation:</strong> 
- The optimal split is into [1,2,3] and [4,5], where the largest sum is 9.
</pre>

### <strong class="example">Example 3:</strong>

<pre>
<strong>Input:</strong> nums = [1,4,4], k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
- The optimal way to split the array is into [1], [4], [4], where the largest sum is 4.
</pre>

### Constraints:

<ul>
    <li><code>1 <= nums.length <= 1000</code></li>
    <li><code>0 <= nums[i] <= 10<sup>6</sup></code></li>
    <li><code>1 <= k <= min(50, nums.length)</code></li>
</ul>

---
