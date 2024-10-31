#include <limits.h>

int reverse(int x) {
    int sum = 0;

    while (x != 0) {
        int rem = x % 10; // Get the last digit
        x /= 10; // Remove the last digit

        // Check for overflow/underflow
        if (sum > (INT_MAX / 10) || (sum == INT_MAX / 10 && rem > 7)) return 0;
        if (sum < (INT_MIN / 10) || (sum == INT_MIN / 10 && rem < -8)) return 0;

        sum = sum * 10 + rem; // Build the reversed number
    }

    return sum;
}
