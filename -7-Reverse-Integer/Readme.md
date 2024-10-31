🔄 Reverse Integer
👋 Welcome to the Reverse Integer project! This function takes an integer, reverses its digits, and handles overflow and underflow situations. Let’s dive into the details! 🏊‍♂️

📚 Problem Statement
Given a 32-bit signed integer x, reverse the digits of x. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

🛠️ Constraints
The input integer x is in the range of [-2^31, 2^31 - 1].

🌟 Example
Example 1
Input:

x = 123
Output:

321
Example 2
Input:

x = -123
Output:

-321
Example 3
Input:

x = 120
Output:

21
Example 4
Input:

x = 0
Output:

0
🚀 How It Works
Initialization:

Initialize sum to 0 to build the reversed number.

Digit Extraction and Reversal:

In a loop, extract the last digit of x using x % 10 and then remove the last digit using x /= 10.

Check for overflow/underflow before adding the digit to sum. If overflow/underflow conditions are detected, return 0.

Update sum by adding the extracted digit in the reversed position.

Return Result:

Once all digits are processed, return the reversed number stored in sum.