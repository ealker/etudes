/* 
 * Problem 3: Largest prime factor
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143?
 * 
 * Answer: 6857
 *
 */

import java.util.Iterator;
import java.util.TreeSet;

public class Problem4 {

    public static void main(String[] args) {
        checkProducts();
    }

    private static void checkProducts() {
        final TreeSet<Integer> products = new TreeSet<>();

        for (int x = 999; x >= 100; x--) {
            for (int y = 999; y >= 100; y--) {
                products.add(x * y);
            }
        }
        Iterator<Integer> iterator = products.descendingIterator();
        while (iterator.hasNext()) {
            int currentNum = iterator.next();

            if (isPalindrome(currentNum)) {
                System.out.println(currentNum);
                break;
            }
        }
    }


    private static boolean isPalindrome(int val){
        String s = String.valueOf(val);
        return new StringBuilder(s).reverse().toString().equals(s);
    }
}


