<h2><a href="https://leetcode.com/problems/valid-parenthesis-string">Valid Parenthesis String</a></h2> 
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given a string <code>s</code> containing only three types of characters: '(', ')', and '*', return <code>true</code> if <code>s</code> is valid.</p>

<p>The following rules define a valid string:</p>
<ul>
    <li>Any left parenthesis '(' must have a corresponding right parenthesis ')'.</li>
    <li>Any '*' can be treated as a single right parenthesis ')', a single left parenthesis '(', or an empty string.</li>
    <li>An empty string is also valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "(*)"
<strong>Output:</strong> true
<strong>Explanation:</strong> The '*' can be treated as a single right parenthesis ')'.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "(*))"
<strong>Output:</strong> true
<strong>Explanation:</strong> The '*' can be treated as a single left parenthesis '(' and the second ')' closes the first '('.
</pre>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= s.length &lt;= 100</code></li>
    <li><code>s[i] is '(', ')' or '*'</code></li>
</ul>

<h3>Intuition</h3>
<p>To determine if the string is valid, we can use a two-pointer approach. Since we know that every opening parenthesis must have a corresponding closing parenthesis, we need to ensure that the counts of each type of parenthesis are balanced.</p>

![image](https://assets.leetcode.com/users/images/c9963c0a-116b-421c-a3db-f056275d32ec_1712495340.6188605.png)

<p>By using two pointers, we can traverse the string from both ends. We will maintain counts of the opening and closing parentheses while considering the '*' as a wildcard character that can represent either type of parenthesis or nothing at all. This leads to a systematic way to check for balance without generating all possible combinations.</p>

<h3>Algorithm</h3>
<ol>
    <li>Define base conditions to optimize the solution:
        <ul>
            <li>If <code>s.size()</code> is odd, return <code>false</code> since an unequal number of parentheses can never be balanced.</li>
            <li>If <code>s.size() is 1</code>, return <code>false</code> since a single parenthesis cannot be balanced.</li>
        </ul>
    </li>
    <li>Initialize two variables, <code>left</code> and <code>right</code>, to store counts of opening and closing parentheses respectively.</li>
    <li>Count opening parentheses starting from the beginning of the string, incrementing <code>left</code> for '(' or '*' (unlocked). For ')', decrement <code>right</code>.</li>
    <li>Count closing parentheses starting from the end of the string, incrementing <code>right</code> for ')' or '*' (unlocked). For '(', decrement <code>right</code>.</li>
    <li>If at any point <code>left</code> or <code>right</code> becomes negative, it indicates an imbalance, and we can return <code>false</code>.</li>
    <li>If we traverse the string without any imbalances, return <code>true</code>.</li>
</ol>

<h3>Complexity</h3>
<ul>
    <li>Time complexity: <code>O(n)</code></li>
    <li>Space complexity: <code>O(1)</code></li>
</ul>
