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
            
    

    def checkForNumber(self,value):       
        reverse = 0
        check = value
        while check != 0: 
            digit = check % 10
            reverse = reverse * 10 + digit       
            check = check//10   
        if value == reverse:
            print('Value is palindrome')
        else:
            print('Value is not palindrome')


num = numbers()
num.checkPalindrome('xyx')