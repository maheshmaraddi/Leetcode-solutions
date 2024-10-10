<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/">Best Time to Buy and Sell Stock IV</a></h2>  
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>You are given an array <code>prices</code>, where <code>prices[i]</code> represents the stock price on the <code>i<sup>th</sup></code> day. You are also given an integer <code>k</code>, which is the maximum number of transactions you can make.</p>

<p>Your goal is to find the maximum profit you can achieve with at most <strong>k transactions</strong>.</p>

<p><strong>Note:</strong> A transaction consists of buying a stock on one day and selling it on another day later on. You cannot hold more than one stock at a time, meaning you must sell the stock before buying again.</p>

<p>&nbsp;</p>

### Explanation:

- **Prices Array**: The array `prices[i]` gives the stock price on each day.
- **Transaction**: A transaction is when you buy a stock and then sell it on a later day. You want to maximize your profit by completing at most `k` transactions.
- **Goal**: You must calculate the maximum profit you can get by buying and selling stocks, without doing more than `k` transactions.

---

### <strong class="example">Example 1:</strong>

<pre>
<strong>Input:</strong> prices = [3,3,5,0,0,3,1,4], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
- Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3 - 0 = 3.
- Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4 - 1 = 3.
- Total profit = 6 (3 + 3).
</pre>

### <strong class="example">Example 2:</strong>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
- Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5 - 1 = 4.
- Note: You can’t buy on day 1 and day 2 at the same time. You must sell the first stock before buying again.
</pre>

### <strong class="example">Example 3:</strong>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1], k = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
- In this case, no transaction is possible since the prices only decrease. So, the maximum profit is 0.
</pre>

### Constraints:

<ul>
	<li><code>1 <= prices.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= prices[i] <= 10<sup>5</sup></code></li>
	<li><code>1 <= k <= 100</code></li>
</ul>

---
