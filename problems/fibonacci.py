'''
A recursive function to return the first n numbers in the fibonacci sequence
'''

def fib(num, num1 = 0, num2 = 1, count = 0):
    if count == 0:
        print(num1)
        count += 1
    print(num2)
    count += 1
    if count == num:
        return
    else:
        temp = num1
        num1 = num2
        num2 = temp + num1
        return fib(num, num1, num2, count)
    
    
print("Enter '0' to stop.")
num = int(input('Enter a number: '))
while num != 0:
    print('Fibonacci Sequence')
    fib(num)
    print()
    num = int(input('Enter a number: '))
