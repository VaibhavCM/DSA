def isPalindrome(x):
    s=str(x)

    i=0
    j=len(s)-1

    while i<j:
        if s[i]!=s[j]:
            print("This is not palindrome")
            return False

        else:
            i+=1
            j-=1

    return True

print(isPalindrome("ggdag"))

