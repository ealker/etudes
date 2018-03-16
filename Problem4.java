/* 
 * Problem 4: Largest palindrome product
 * A palindromic number reads the same both ways. 
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 * 
 * Answer: 906609
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


