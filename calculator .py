while(1):
    print("SIMPLE CALCULATOR")
    number1=int(input("enter the number1: "))
    number2=int(input("enter the number2: "))
    print("enter your operation which you want: \n")
    print("\n 1.sum\n2.subratct\n3.multiple\n4.divide\n5.square\n6.sqrt\n7.power\n8.greater and lesser")
    operator=int(input("enter the operator: "))

    if operator==1:
        sum=number1+number2
        print("the sum is ",sum)
    elif operator==2:
        subract=number1-number2
        print("the subract is ",subract)
    elif operator==3:
        multiple=number1*number2
        print("the multiple is ",multiple)
    elif operator==4:
        if number2!=0:
            divide=number1/number2
            print("the division of the number is ",divide)
        else:
            print("Not possible")
            
    elif operator==5:
        square1=number1*number1
        square2=number2*number2
        print("the square 1st number is ",number1*number1,"\nthe square of the second number is ",number2*number2)
    elif operator==6:
        for i in range(0,number1):
            if i*i==number1:
                print("the sqrt of num 1: ",i)

        for j in range(0,number2):
            if j*j==number2:
                print("the sqrt of num 2: ",j)

    elif operator==7:
        power=number1**number2
        print("the power is ",power)

    elif operator==8:
        if number2>number1:
            print("the number2 is greater")
        else:
            print("the number1 is greater")

    else:
        print("invalid operator\nTRY AGAIN")


    choice = input("Enter the choice if you want continue (enter y or Y): ")

    if choice=="y"  or choice=="Y":
        continue
    elif choice=="n" or choice=="N":
        print("\nyour program stops here")
        break
    else:
        print("\n ERROR HAPPENS PLEASE TRY AGAIN ONCE")
        break