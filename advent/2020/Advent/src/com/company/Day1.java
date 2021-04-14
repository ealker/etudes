package com.company;

import com.company.utils.Input;

import java.util.ArrayList;
import java.util.Collections;

public class Day1 {

    public int solution() {

        // Get input from file.
        Input input = new Input();
        ArrayList<Integer> nums = input.getFileInput(1);

        //Setup target and answer variable.
        int answer = 0;
        int target = 2020;
        ArrayList<Integer> twoNums = new ArrayList<>();

        //Sort the input array in ascending order.
        Collections.sort(nums);

        //Two pointers technique. Searching for pairs in a sorted array.
        int i = 0;
        int j = nums.size() - 1;

        while (i < j) {

            if (nums.get(i) + nums.get(j) == target) {
                twoNums.add(nums.get(i), nums.get(j));
            } else if (nums.get(i) + nums.get(j) < target) {
                i++;
            } else {
                j--;
            }
            return answer;
        }
        return answer;
    }
}
