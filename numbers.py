
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

      #GCD of two numbers  
    def GCD(self,val1,val2):
        if val2==0:
            return val1
        return self.GCD(val2,val1%val2)
    # LCM of tow numbers
    def LCM(self ,val1,val2):
        return val1*val2/self.GCD(val1,val2)

    #fibonacci series
    def fibonacci(self,value):
        first =0
        second=1
        if value <=0:
            return print('Please enter positive integer')
        elif value == 1:
            return first
        else:
            print(first)
            print(second)
            for i in range(2,value):
                next = first+second
                first =second
                second= next
                print(f'{next}  {i}')


num = numbers()
#num.checkPalindrome(121)
#num.reverse(113)
#print(num.GCD(18,12))
#print(num.LCM(30,20))
#num.fibonacci(5)