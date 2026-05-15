queue=[]
front=-1
rear=-1
n=int(input("enter the no of  elements: "))
while(1):
    choice=int(input(" which operation you want: 1.push \n 2.pop \n 3.display \n 4.exit \n enter your choice: "))

    if choice==1:
        if rear==n-1:
            print("Queue is Overflow: ")
        else:
            for i in range(n):
                values=int(input("enter the values: "))
                rear=rear+1
                queue=queue+[values]

                if front==-1:
                    front=0

                print("value inserted")
    elif choice==2:
        if front==-1 or front>rear:
            print("queue is in underflow")
        else:
            print("the deleted elements are: ",queue[front])
            front=front+1

    elif choice==3:
        if front==-1 or front>rear:
            print("queue is in underflow")

        else:
            i=front
            while i<rear+1:
                print("the displayed all numbers are: ",queue[i])
                i+=1

    elif choice==4:
        print("program is  termianted here")
        break

                


