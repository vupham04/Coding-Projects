<h1>Maze Solver</h1>

What's more fun than solving a maze? Writing a program to solve a maze! This problem asks you to write a program that reads in a textual description of a maze and either produces output that shows the solution to the maze or indicates that the maze has no solution.

One way to describe a maze using text is to use one character ('X') to represent walls and spaces (' ') to represent hallways. Further, the starting point of the maze can be indicated by an 'S' and the exit by an 'E'. There is always exactly one entrance and one exit.

A solution to the maze can be indicated by placing period ('.') characters along the path from the start to the exit.

Notice that the solution above still contains empty spaces. Such areas may be explored when searching for a path through the maze. However, the reported solution for a maze must progresses directly from the start to the exit without ever entering a dead-end.

Every maze on which your program is tested will have at most one solution.

<h2>Input Format</h2>

The first line of the input will contain 2 comma delimited integers, r and c, that indicate the number of rows and columns in the maze. The remainder of the input contains one line for each row in the maze. The line for each row contains one character for each column in the maze. Each of these lines may contain only the following characters:

'X' - a wall.

'S' - the starting point.

'E' - the ending point.

' ' - a hallway.

<h2>Constraints</h2>

1 <= r <= 15

1 <= c <= 15

<h2>Output Format</h2>

If the maze does not have a solution the output will be the single line:

No Solution!

If the maze does have a solution the output will display the maze exactly as in the input but with spaces (' ') replaced by periods ('.') to indicate the path taken. The output will not include the first line of the input indicating the number of rows and columns in the maze.

<h3>Sample Input 0<h3>
<p/>5,5<br/>
XSXXX<br/>
X X X<br/>
X   X<br/>
X X X<br/>
XXXEX<br/>
<h3>Sample Output 0</h3>
XSXXX<br/>
X.X X<br/>
X...X<br/>
X X.X<br/>
XXXEX<br/>
<h3>Sample Input 1</h3>
5,5<br/>
XSXXX<br/>
X   X<br/>
X XXX<br/>
X X X<br/>
XXXEX<br/>
<h3>Sample Output 1</h3>
No Solution!<br/>
