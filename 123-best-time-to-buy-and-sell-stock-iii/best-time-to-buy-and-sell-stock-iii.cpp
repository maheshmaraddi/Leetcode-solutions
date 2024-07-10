class Solution {
public:
    int memoization(vector<int>& prices, int currDay, int transactionsLeft,
                    vector<vector<int>>& mem) {
        if (currDay == prices.size() or transactionsLeft == 0)
            return 0;

        if (mem[currDay][transactionsLeft] == -1) {
            int ans1 = memoization(prices, currDay + 1, transactionsLeft, mem),
                ans2;
            if (transactionsLeft % 2) // sell
                ans2 = memoization(prices, currDay + 1, transactionsLeft - 1,
                                   mem) +
                       prices[currDay];
            else // buy
                ans2 = memoization(prices, currDay + 1, transactionsLeft - 1,
                                   mem) -
                       prices[currDay];

            mem[currDay][transactionsLeft] = max(ans1, ans2);
        }

        return mem[currDay][transactionsLeft];
    }

    int maxProfit(vector<int>& prices) {
        vector<vector<int>> mem(prices.size(), vector<int>(5, -1));//mem[i][j] stores profit after day i with j transactions left
        return memoization(prices, 0, 4, mem);
    }
};