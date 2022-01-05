
class numbers:
    # Check Palindrome for string and numbers 
    def checkPalindrome(self,value):
        if type(value) is str:
            reverse = value[::-1]
            if value == reverse:
                print('Value is palindrome')
            else:
                print('Value is not palindrome')
        elif type(value) is int:
            self.checkForNumber(value)
        else:
            print('Please enter valid number floats and booleans are not allowed')
            
    
    #Palindrome for number
    def checkForNumber(self,value):       
        reverse = self.reverse(value)
        if value == reverse:
            print('Value is palindrome')
        else:
            print('Value is not palindrome')
    
    #reverse a number
    def reverse(self,value)->int:
        reverse = 0
        check = value
        while check != 0: 
            digit = check % 10
            reverse = reverse * 10 + digit       
            check = check//10
         
        return reverse
    def GCD(self,val1,val2):
        if val2==0:
            return val1
        return self.GCD(val2,val1%val2)
    
    def LCM(self ,val1,val2):
        return val1*val2/self.GCD(val1,val2)
        

num = numbers()
#num.checkPalindrome(121)
#num.reverse(113)
print(num.GCD(18,12))
print(num.LCM(30,20))
