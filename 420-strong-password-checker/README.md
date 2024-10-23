<h2><a href="https://leetcode.com/problems/strong-password-checker/">Strong Password Checker</a></h2>  
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>A password is considered strong if the below conditions are all met:</p>

    It has at least 6 characters and at most 20 characters.
    It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
    It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).

<p>Given a string <code>password</code>, return the minimum number of steps required to make the password strong. If the password is already strong, return <code>0</code>.</p> <p>In one step, you can:</p>

    Insert one character to the password,
    Delete one character from the password, or
    Replace one character of the password with another character.

<strong class="example">Example 1:</strong>
<pre> <strong>Input:</strong> password = "a" <strong>Output:</strong> 5 </pre>
<strong class="example">Example 2:</strong>
<pre> <strong>Input:</strong> password = "aA1" <strong>Output:</strong> 3 </pre>
<strong class="example">Example 3:</strong>
<pre> <strong>Input:</strong> password = "1337C0d3" <strong>Output:</strong> 0 </pre>
Constraints:
<ul> <li><code>1 <= password.length <= 50</code></li> <li><code>password</code> consists of letters, digits, dot <code>'.'</code> or exclamation mark <code>'!'</code>.</li> </ul>

