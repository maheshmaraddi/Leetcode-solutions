
<h2><a href="https://leetcode.com/problems/split-array-largest-sum/">Split Array Largest Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Hard' /><hr>
<p>Time:Runtime=0ms,Beats=100% , Space: Memory=9.22MB,Beats=89.11</p>
<p>You are given an array nums and a integer k,you have to split this Array nums into k pieces and return the largest sum of subarray</p>
<h3>Explanation:</h3>
<ul>
<li>we know that The Smallest Possible result is the largest element of array</li>
<li>we also know that The Largest Possible result is the Sum of all Elements of array</li>
<li>Now,we Have the Range in Which Our Answer is lie.</li>
<li>So,we use Binary Search to get our Answer,But in binary Search After Deckaration of mid we create a Count Function this count function count the pieces whose sum is less then or equal to mid and return this value of pieces to variable pieces in binary Search</li>
<li>Then,if The Value of pieces is less then or equal to k then end(e) is equal to mid , else start(s) is equal to mid+1</li>
<li>After Completion the while loop of Binary Search you have to return e and we get our Answer.<li>
</ul>
