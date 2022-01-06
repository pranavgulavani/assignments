
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
    #check prime
    def checkPrime(self,value):
        if value <= 0 or value==1:
            return False
        counter =0
        
        for i in range(2,value+1):
            if value % i == 0:
                counter += 1
            if counter >= 2:
                return False
        
        return True   
    
    #find numbers in given number of series
    def findPrime(self,listOfNumbers):
        primes = []
        for index in range(len(listOfNumbers)):
            check = self.checkPrime(listOfNumbers[index])
            if check == True:
                primes.append(listOfNumbers[index])
        return primes

   
    #num is sum of two primes
    def checknum(self,num):
        for i in range(num+1):
            check = self.checkPrime(i)
            if check and i <= num//2:
                value = num- i
                checknext = self.checkPrime(value)
                if checknext:
                    print(i,value)
                


num = numbers()
#num.checkPalindrome(121)
#num.reverse(113)
#print(num.GCD(18,12))
#print(num.LCM(30,20))
#num.fibonacci(5)
#val =num.checkPrime(10)
#print(val)
values = [101, 7, 9, 3, 1, 91, 97, 555]
val =num.findPrime(values)
print(val)
#num.checknum(8)