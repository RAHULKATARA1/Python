a = int(input("enter the number 1 :- "))
b = int(input("enter the number 2 :- "))
c = int(input("enter the number 3 :- "))


if(a>=b and a>=c):
    print("first number is the largest - ",a)
elif(b>c):
    print("second number is the largest ", b)
else:
    print("third number is the largest  ",c)
