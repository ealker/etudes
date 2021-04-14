package com.company.utils;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Input {

    public ArrayList<Integer> getFileInput(int dayNum){
        String filename = "resources/day" + dayNum + ".txt";
        File file = new File(filename);
        ArrayList<Integer> input = new ArrayList<>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line = reader.readLine();
            while (line != null) {
                input.add(Integer.parseInt(line));
                System.out.println(line);
                line = reader.readLine();
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Cannot parse input file.");
        }
        return input;
    }
}
