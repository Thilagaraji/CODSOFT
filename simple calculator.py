import math
def add(list):
    a=sum(list)
    return a
def subs(list):
  i=0
  s=list[i]
  for j in range(1,len(list),1):
    s=s-list[j]
  return s
def mult(list):
    m=1
    for i in list:
        m=m*i
        
    return m
def dir(x,y):
    return x/y
print("1.add\n2.sub\n3.mult\n4.div\n5.exit")

while True:
    ch=input("Enter choice(1/2/3/4/5):")
    if ch in ('1','2','3'):
        list=[int(item) for item in input("Enter the list of elements to perform operation :").split()]
        print(list)
    if ch in ('1','2','3','4','5'):
        if ch=='1':
            print("sum of numbers :",add(list))
        elif ch=='2':
            print("the Result is:",subs(list))
            
        elif ch=='3':
            print("Multiplication of numbers is:",mult(list))

        elif ch=='4':
            a=float(input("enter the divisor:"))
            b=float(input("enter the dividend:"))
            print("divition of num:",dir(a,b))
        elif ch=='5':
            print("thanks for using")
    
            break
        else:
            print("invaild enter,pls enter the vaild value")
            break
