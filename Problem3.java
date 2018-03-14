import java.util.Iterator;
import java.util.Scanner;
import java.util.TreeSet;

public class Problem3 {

    public static void main(String[] args) {

        System.out.println("Please enter a number: ");
        Scanner scanner = new Scanner(System.in);
        long inputValue = scanner.nextLong();
        int inputSqrt = (int) Math.round(Math.sqrt(inputValue)); //We only have to find everything up to the square root of the input.
        System.out.println("The largest prime factor is: ");
        System.out.println(largestPrimeFactor(primeSieve(inputSqrt),inputValue));
    }


    public static Iterator<Integer> primeSieve(long inputMax) {

        final TreeSet<Integer> results = new TreeSet<>(); //TreeSet with Comparator provides total ordering of elements.

        results.add(2);

        for (int i = 3; i < inputMax; i += 2) {
            results.add(i);
        }

        Integer currentValToCompare = results.first();
        while((currentValToCompare = results.higher(currentValToCompare)) != null){
            for(int i = currentValToCompare * 2; i <= inputMax; i+= currentValToCompare){
                results.remove(i);
            }
        }

        return results.descendingIterator();
    }

    private static int largestPrimeFactor(Iterator<Integer> primeNums, long inputVal) {
        while(primeNums.hasNext()) {
            final int prime = primeNums.next();
            if (inputVal % prime == 0) {
                return prime;
            }
        }
        return 0;
    }
}


