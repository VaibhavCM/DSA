# count how many vowels in the word

value=input("enter the input word you want to count the vowels in the word: ")

vowels=['a','e','i','o','u'] 

count=0

for letters in value:
    if letters in vowels:
        print("vowels found")
        count+=1
        print("the vowels are ",count)
        break
else:
    print("not found")


    