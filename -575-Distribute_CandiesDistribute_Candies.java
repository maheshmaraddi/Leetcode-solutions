// src/com/example/distributecandies/DistributeCandies.java

import java.util.HashSet;

public class DistributeCandies {
    public int distributeCandies(int[] candyType) {
        HashSet<Integer> uniqueCandies = new HashSet<>();
        for (int candy : candyType) {
            uniqueCandies.add(candy);
        }
        return Math.min(uniqueCandies.size(), candyType.length / 2);
    }

    public static void main(String[] args) {
        DistributeCandies solution = new DistributeCandies();

        int[] candyType1 = {1, 1, 2, 2, 3, 3};
        System.out.println(solution.distributeCandies(candyType1)); // Output: 3

        int[] candyType2 = {1, 1, 2, 3};
        System.out.println(solution.distributeCandies(candyType2)); // Output: 2
    }
}

