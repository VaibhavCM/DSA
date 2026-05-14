print("*******************STACK OPERATION**********************")
n=int(input("enter the no of elements: "))
top=-1
stack=[]
for i in range(n):
        stack=stack+[None]
while(1):
    print("\n enter the choice: \n1.push \n2.pop \n3.display \n4.exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        if top==n-1:
            print("stack overflow")
        else:
            for i in range(n):
                value=int(input("enter the values: "))
                top+=1
                stack[top]=value
            print("Values inserted successfully")
    elif choice==2:
        if top==-1:
            print("stack underflow")
        else:
            print("\n the deleted element is: ",stack[top])
            stack[top]=None
            top=top-1
    elif choice==3:
        if top==-1:
            print("stack underflow")
        else:
            while i>=0:
                print("the elments are: ",stack[i])
                i-=1
    elif choice==4:
        print("your program terminated here")
        break
