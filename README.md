# Recursion
Recursion is a programming technique where a function calls itself, either directly or indirectly. It is a powerful and elegant approach to solving problems that involve repetitive subtasks.\

Recursion is used in a variety of programming applications, such as searching and sorting algorithms, tree traversal, and mathematical computations. However, it is important to be careful when using recursion, as it can lead to stack overflow errors if not implemented correctly. Additionally, recursive algorithms can sometimes be less efficient than their iterative counterparts.

## What is the Call Stack?
The call stack is a data structure used by a computer program to keep track of the sequence of function calls made during the execution of the program.\

When a function is called, the program pushes a stack frame onto the call stack, which contains information about the function's arguments, local variables, and the location in the program where the function was called from. The program then jumps to the beginning of the called function, executes its code, and when the function returns, the program pops the stack frame off the call stack and returns to the location in the program where the function was called from.\

The call stack is important because it allows the program to keep track of where it is in the execution of the program and to maintain the state of each function as it is called and returned from. It also helps to prevent stack overflow errors, which occur when the call stack becomes too large and overflows the available memory.

## Recursive Methods/Functions
A recursive function is a function which calls itself. It typically has two parts: a base case and a recursive case. 

### Base Case
The base case is the stopping condition for the recursion, where the function does not call itself and returns a result. In other words, this is where the input is directly solveable and there is no further recursive call.

### Recursive Case/Call
The recursive case is where the function calls itself, passing a modified version of the problem to solve.

### What happens when a recursive method is called?
When a recursive function is called, it creates a new instance of itself on the call stack. Each instance of the function has its own set of variables and parameters. As the recursion proceeds, the call stack grows deeper, with each recursive call adding a new frame to the stack.

## Rules of Recursion
1. Your code must have a case for ALL valid inputs.
2. You must have base cases.
3. When you make a recursive call, it should be to a simpler instance of the same problem and make forward progress towards the base case.

## Complexity Analysis
### Methods
There are 3 ways of calculating the complexity of a recursive algorithm:
1. Recursive Tree Drawing
* Draw a recursive tree and calculate the time taken by each level of the tree.
* Sum the work done at all levels
2. Recurrence Relation Unfolling
* Substitute values into therecurrence relation.
* Deduce a general formula for the time complexity
3. Master Theorem

