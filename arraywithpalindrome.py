class Solution:
    def isPalinArray(self, arr):
        for num in arr:
            original = num
            reverse = 0
            
            while num > 0:
                digit = num % 10
                reverse = reverse * 10 + digit
                num = num//10
                
            if original != reverse:
                return 0
                
        return 1
        
        