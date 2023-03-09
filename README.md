# Recursion
Recursion is a programming technique where a function calls itself, either directly or indirectly. It is a powerful and elegant approach to solving problems that involve repetitive subtasks.\

Recursion is used in a variety of programming applications, such as searching and sorting algorithms, tree traversal, and mathematical computations. However, it is important to be careful when using recursion, as it can lead to stack overflow errors if not implemented correctly. Additionally, recursive algorithms can sometimes be less efficient than their iterative counterparts.

# What is the Call Stack?
The call stack is a data structure used by a computer program to keep track of the sequence of function calls made during the execution of the program.\

When a function is called, the program pushes a stack frame onto the call stack, which contains information about the function's arguments, local variables, and the location in the program where the function was called from. The program then jumps to the beginning of the called function, executes its code, and when the function returns, the program pops the stack frame off the call stack and returns to the location in the program where the function was called from.\

The call stack is important because it allows the program to keep track of where it is in the execution of the program and to maintain the state of each function as it is called and returned from. It also helps to prevent stack overflow errors, which occur when the call stack becomes too large and overflows the available memory.

## Recursive Methods
A recursive function typically has two parts: a base case and a recursive case. 

### Base Case
The base case is the stopping condition for the recursion, where the function does not call itself and returns a result. 

### Recursive Case
The recursive case is where the function calls itself, passing a modified version of the problem to solve.

### What happens when a recursive method is called?
When a recursive function is called, it creates a new instance of itself on the call stack. Each instance of the function has its own set of variables and parameters. As the recursion proceeds, the call stack grows deeper, with each recursive call adding a new frame to the stack.

