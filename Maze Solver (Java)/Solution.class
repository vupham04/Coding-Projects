import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

   public static boolean solveTheMaze(char[][] theMaze, int startR, int startC) {
        if (startR < 0 || startR >= theMaze.length || startC < 0 || startC >= theMaze[0].length) {
            return false;
        }

        if (theMaze[startR][startC] == '.' || theMaze[startR][startC] == 'X') {
            return false;
        }

        if (theMaze[startR][startC] == 'E') {
            return true;
        }

        if (theMaze[startR][startC] == ' ') {
            theMaze[startR][startC] = '.';
        }

        if (solveTheMaze(theMaze, (startR - 1), startC)) {
            return true;
        }

        if (solveTheMaze(theMaze, (startR + 1), startC)) {
            return true;
        }

        if (solveTheMaze(theMaze, startR, startC + 1)) {
            return true;
        }

        if (solveTheMaze(theMaze, startR, startC - 1)) {
            return true;
        }

        if (theMaze[startR][startC] == '.') {
            theMaze[startR][startC] = ' ';
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        // determine the number of rows and columns
        String[] startAndEnd = scr.nextLine().split(",");
        int rows = Integer.valueOf(startAndEnd[0]);
        int columns = Integer.valueOf(startAndEnd[1]);

        // the Start (S) point
        int startR = -1;
        int startC = -1;

        // reconstruct the maze to a 2-D array
        char[][] theMaze = new char[rows][columns];
        for (int r = 1; r <= rows; r++) {
            String theRowsValue = scr.nextLine();
            char[] theRows = theRowsValue.toCharArray();
            for (int c = 1; c <= columns; c++) {
                theMaze[r - 1][c - 1] = theRows[c - 1];

                // determine the starting point
                if (theMaze[r - 1][c - 1] == 'S') {
                    startR = r - 1;
                    startC = c - 1;
                }
            }
        }

        boolean solve = solveTheMaze(theMaze, startR, startC);
        if (solve) {
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < columns; j++) {
                    System.out.print(theMaze[i][j]);
                }
                System.out.println("");

            }
        } else {
            System.out.println("No Solution!");
        }

        scr.close();
    }
}