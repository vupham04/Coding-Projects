import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class FerryBoat {

    int l; // total length of cars that the ferry can carry, meters
    int n; // number of cars wait to cross the river
    LinkedList<Car> leftCar;
    LinkedList<Car> rightCar;

    static int COUNT = 1; // count the trip
    static boolean SIDE = false;        // the side of the boat - left is false, right is true

    public FerryBoat() {
        l = 0;
        n = 0;
        leftCar = new LinkedList<>();
        rightCar = new LinkedList<>();
    }

    public static void main(String[] args) {
        FerryBoat f = new FerryBoat();
        f.readInput(new Scanner(System.in));
        f.solveProblem();
    }

    public void readInput(Scanner s) {
        String nL = s.nextLine();
        String[] nAndL = nL.split(" ");
        l = Integer.valueOf(nAndL[0])*100;        // *100 to convert from meters to centimeters
        n = Integer.valueOf(nAndL[1]);

        for (int i = 0; i < n; i++) {
            String oneLine = s.nextLine().trim();
            String[] oneLineArray = oneLine.split(" ");
            int length = Integer.valueOf(oneLineArray[0]);
            String plate = oneLineArray[1];
            String direction = oneLineArray[2];
            
            Car car = new Car(length, plate);
            
            if (direction.equals("left")) {
                leftCar.add(car);
            } else {
                rightCar.add(car);
            }
        }
    }

    public void solveProblem() {
        if(n==0) {
            System.out.println("Day Off!");
        } else if(leftCar.size()>0 || rightCar.size()>0|| SIDE){
            int remainLength = l;
            ArrayList<Car> carForTrip = new ArrayList<>();
            if(SIDE && rightCar.size()>0) {
                while(remainLength>=rightCar.peek().length) {
                    Car carToAdd = rightCar.poll();
                    carForTrip.add(carToAdd);
                    remainLength -= carToAdd.length;
                    if(rightCar.size()==0) {
                        break;
                    }
                }
            } else if(!SIDE&& leftCar.size()>0) {
                while(remainLength>=leftCar.peek().length) {
                    Car carToAdd = leftCar.poll();
                    carForTrip.add(carToAdd);
                    remainLength -= carToAdd.length;
                    if(leftCar.size()==0) {
                        break;
                    }
                }
            }
            
            printTrip(carForTrip);
            SIDE = !SIDE;
            solveProblem();
        }
    }

    private void printTrip(ArrayList<Car> c) {
        if (c.size() == 0) {
            System.out.println(COUNT + " : empty");
        } else {
            System.out.print(COUNT + " :");
            for (Car car : c) {
                System.out.print(" " + car.plate);
            }
            System.out.println();    
        }
        COUNT++;
    }

    public static class Car {

        int length;
        String plate;

        public Car(int l, String p) {
            length = l;
            plate = p;
        }
    }

}