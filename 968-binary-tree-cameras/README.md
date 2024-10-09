You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.


Example 1:

![image](https://github.com/user-attachments/assets/4bfba176-b2fd-4863-9481-90e3129ddb3a)

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

![image](https://github.com/user-attachments/assets/de49fb6f-e2a9-4c39-912e-2e42100662b7)

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    Node.val == 0

