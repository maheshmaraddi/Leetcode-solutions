🚀 Add Two Numbers 🧮 (MEDIUM)
👋 Welcome to the Add Two Numbers project! This is a fun and handy implementation where we add two non-negative integers represented as linked lists. The digits are stored in reverse order, and each of their nodes contains a single digit. Let's dive in! 🏊‍♂️

📚 Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

🛠️ Constraints
The number of nodes in each linked list is in the range [1, 100].

Each Node.val is between 0 and 9.

No leading zeros except for the number 0 itself.

🌟 Example
Example 1
Input:

l1 = [2,4,3]
l2 = [5,6,4]
Output:

[7,0,8]
Explanation: 342 + 465 = 807, and 807 in reverse order is 708.

Example 2
Input:

l1 = [0]
l2 = [0]
Output:

[0]
Explanation: 0 + 0 = 0.

Example 3
Input:

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
Output:

[8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998, and 10009998 in reverse order is 89990001.

🚀 How It Works
Initialization:

A dummy_head node is created to simplify the process of building the result list.

current keeps track of the current node in the new list.

carry handles the carry-over in addition.

Iteration:

The loop runs while there are still nodes in either l1 or l2.

x and y are the values of the current nodes of l1 and l2 respectively (default to 0 if the node is None).

total is the sum of x, y, and carry.

carry is updated to be the result of integer division of total by 10.

A new node is added to the result list with the value total % 10.

Advance Nodes:

Moves to the next nodes in l1 and l2.

Handling Remaining Carry:

After the loop, if there's any carry left, it adds it as a new node.

Return Result:

Returns the result list starting from the node following dummy_head.