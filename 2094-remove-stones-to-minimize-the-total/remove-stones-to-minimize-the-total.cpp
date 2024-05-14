#include <queue>
#include <cmath>
#include <vector>

class Solution {
public:
    int minStoneSum(std::vector<int>& piles, int k) {
        // Create a max heap
        std::priority_queue<int> max_heap;
        for (int pile : piles) {
            max_heap.push(pile);
        }
        
        // Perform k operations
        while (k--) {
            // Fetch the maximum value from the heap
            int max_val = max_heap.top();
            max_heap.pop();
            // Calculate the new value after operation
            int new_val = max_val - std::floor(max_val / 2);
            // Push the new value back to the heap
            max_heap.push(new_val);
        }
        
        // Calculate the sum of remaining values in the heap
        int sum = 0;
        while (!max_heap.empty()) {
            sum += max_heap.top();
            max_heap.pop();
        }
        
        return sum;
    }
};
