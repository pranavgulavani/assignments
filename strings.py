class strings:

    #Remove any given character from string
    def removeChar(self,value,character,newCharacter,ocuurence=1)-> str:
        try:
            newValue = value.replace(character,newCharacter,ocuurence)
            return newValue
        except:
            print("exception occured enter string input")

    #concatinate two strings   
    def concat(self,value1,value2)-> str:
        try:
            value3 = str(value1) + str(value2)
            return value3
        except:
            print("Check your input")
    
    #Given a string, reverse each word in the sentence
    def reverseWord(self,value):
        newString = value.split()
        for i in range(len(newString)):
            newString[i] = newString[i][::-1]
        
        return '  '.join(newString)
          

val = strings()
#print(val.removeChar('Hello','l','o'))
#print(val.concat('Hel','lo'))
#value = val.reverseWord("hello")
#print(value)