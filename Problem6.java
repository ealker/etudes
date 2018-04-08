/* 
 * Problem 6: Sum square difference
 * The sum of the squares of the first ten natural numbers is:
 * 1^2 + 2^2 + ... + 10^2 = 385
 * The square of the sum of the first ten natural numbers is:
 * (1 + 2 + ... + 10)^2 = 55^2 = 3025
 * Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
 * 3025 − 385 = 2640.
 * Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 * 
 * Answer: 906609
 *
 */
 
public class Problem6 {

    public static void main(String[] args) {
        System.out.println(difference(sumOfSquares(100), squareOfSum(100)));
    }

    private static int sumOfSquares(int input){
        //Sum of squared n integers: (n+1)(2n+1)/6
        int sum = input * (input + 1) * (2 * input + 1) / 6;
        return sum;
    }

    private static int squareOfSum(int input){
        //Sum of n integers: n(n+1)/2
        int sum = input * (input + 1) / 2;
        return sum * sum;
    }

    private static int difference(int sumSquare, int squareSum){
        return squareSum - sumSquare;
    }

}
