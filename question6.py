#write a program to find the maximum of two numbers
n1,n2=map(int,input("Enter two number:").split())
if n1>n2:
    print("maximum is",n1)
elif n1==n2:
    print("both are equal")
else:
    print("maximum is",n2)
