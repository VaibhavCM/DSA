# circumference of the circle  using the dictionary

# here we find the circumference of the circle using the 2*pi*r

print("when you enter the -1 you go to exit: ")
circum={}
while(1):
    radius=int(input("enter the value: "))
    if radius == -1:
        break
    else:
        di={radius:2*3.14*radius}
        circum.update(di)                    # we update the values from the di dictionary with radius and circumference calculation
print(circum)