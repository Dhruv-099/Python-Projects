num1=float(input("Enter num 1"))
op=input("Enter op")
num2=float(input("Enter num 2"))
if op =='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else : print('invalid operator')