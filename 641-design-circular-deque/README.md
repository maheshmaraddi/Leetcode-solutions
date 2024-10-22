# 641. Design Circular Deque

## Status
**Solved**  
**Difficulty:** Medium

## Description
Design your implementation of a circular double-ended queue (deque). The deque supports adding and removing elements from both ends.

Implement the `MyCircularDeque` class with the following methods:

- **MyCircularDeque(int k)**: Initializes the deque with a maximum size of `k`.
- **boolean insertFront(int value)**: Adds an item at the front of the deque. Returns `true` if the operation is successful, or `false` otherwise.
- **boolean insertLast(int value)**: Adds an item at the rear of the deque. Returns `true` if the operation is successful, or `false` otherwise.
- **boolean deleteFront()**: Deletes an item from the front of the deque. Returns `true` if the operation is successful, or `false` otherwise.
- **boolean deleteLast()**: Deletes an item from the rear of the deque. Returns `true` if the operation is successful, or `false` otherwise.
- **int getFront()**: Returns the front item from the deque. Returns `-1` if the deque is empty.
- **int getRear()**: Returns the last item from the deque. Returns `-1` if the deque is empty.
- **boolean isEmpty()**: Returns `true` if the deque is empty, or `false` otherwise.
- **boolean isFull()**: Returns `true` if the deque is full, or `false` otherwise.

## Examples

### Example 1
**Input:**
```plaintext
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

 

## Constraints
- **1 <= k <= 1000**: The maximum size of the deque.
- **0 <= value <= 1000**: The value to be added to the deque.
- **At most 2000 calls** will be made to the following methods:
  - `insertFront`
  - `insertLast`
  - `deleteFront`
  - `deleteLast`
  - `getFront`
  - `getRear`
  - `isEmpty`
  - `isFull`





