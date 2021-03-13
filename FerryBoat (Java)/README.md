<h1>Ferry Boat</h1>

Before bridges were common, ferries were used to transport cars across rivers. River ferries, unlike their larger cousins, run on a guide line and are powered by the river's current. These ferries are typically narrow, so cars drive onto the ferry single file from one end and line up bumper-to-bumper until the next car will not fit, the ferry then crosses the river, and the cars then exit from the other end of the ferry.

Our ferry is about to open for the day and lines of cars have accumulated on both the left and right banks of the river. The ferry Captain lives on the left bank and thus always starts its day at the left bank terminal. Cars are loaded onto the ferry in the order that they arrived. The ferry travels continuously back and forth between the left and right bank until all of the waiting cars have been transported across the river. The ferry must terminate on the left bank after the final car has been transported, so that the Captain can return home at the end of the day.

Your problem is to display the license plates of the cars (if any) that are transported on each of the ferry's trips across the river.

<h2>Input Format</h2>

The first line of input contains two integers L and N separated by a single space. L indicates the total length of cars that the ferry can carry, in meters. N indicates the total number of cars that are waiting to cross the river.

The next N lines provide information about the cars to be transported across the river. Each line will consist of 3 values each separated by a single space. The first value will be an integer indicating the length of the car in centimeters. All cars will be able to fit on the ferry. The second value is a string giving the license plate number of the car. The license plate number will consist of only the characters A-Z and 0-9. The third value will be either the string "left" or the string "right" and indicates if the car is waiting at the left or right bank terminal.

<h2>Constraints</h2>

0 < L <= 100

0 <= N <= 500

<h2>Output Format</h2>

The output will consist of one line for each trip across the river. The line will begin with an integer indicating the trip number. The first trip is 1. The trip number will be followed by a single space and a colon (':') and another space. If one or more cars are being transported on the trip their license plate number will then appear in a space delimited list. If no cars are being transported then the string "empty" will appear following the colon.

If no cars are waiting to cross the river the Captain gets the day off and the output should simply be the string "Day Off!".

<h3>Sample Input 0</h3>

20 3<br/>
380 ABC left<br/>
720 DEF left<br/>
1340 GHI right<br/>

<h3>Sample Output 0</h3>
1 : ABC DEF<br/>
2 : GHI<br/>
<h3>Sample Input 1</h3>
20 3<br/>
1480 ABC left<br/>
720 DEF right<br/>
575 GHI left<br/>
<h3>Sample Output 1</h3>
1 : ABC<br/>
2 : DEF<br/>
3 : GHI<br/>
4 : empty<br/>
<h3>Sample Input 2</h3>
20 0<br/>
<h3>Sample Output 2</h3>
Day Off!
