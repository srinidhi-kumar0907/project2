#Python Program for Fibonacci numbers

def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
       
n = int(input ("Enter the number: "))
print ("Fibonacci series: ")
for n in range(0, n):
    print (fibonacci(n))
