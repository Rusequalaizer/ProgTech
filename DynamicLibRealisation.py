import ctypes
import matplotlib.pyplot as plt
Euler = ctypes.CDLL('./EulerLib/x64/Debug/EulerLib.dll')

print("""
Here you can see the 
value of the Euler 
function within: [-5; 100], 
as well as a graph of the 
first 1000 values of the 
Euler function:""")

xPlot = []
yPlot = []
numbers = []
for i in range(-5, 101, 1):
    numbers.append(i)
for i in range(0 , 1001):
    xPlot.append(i)
    yPlot.append(Euler.euler(i))
for i in range(len(numbers)):
    print(f"{i - 5} -> {Euler.euler(numbers[i])}")
plt.scatter(xPlot, yPlot, 1)
plt.title("The first 1000 values of the Euler function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

print("""
And, of course, you 
can enter the values 
yourself and make 
sure the algorithm 
works (if you want 
to exit their 
program, enter 0 
in the input field):""")
userInput = 15
while (userInput != 0):
    try:
        userInput = int(input("Input n: "))
        if(userInput == 0):
            print("The program has finished its work")
            break
        print(f"{userInput} -> {Euler.euler(userInput)}")
    except:
        print("Bad input, try again")


