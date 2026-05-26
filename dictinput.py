# here we make the dictionary using input

key=input("enter the values: ").split()   # gives the values like name age marks like this

values=input("enter the value: ").split() # gives as following keys hello 20 95 like this

my_dict=dict(zip(key,values))

print(my_dict)