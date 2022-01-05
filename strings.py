class strings:

    #Remove any given character from string
    def removeChar(self,value,character,newCharacter,ocuurence=1)-> str:
        try:
            newValue = value.replace(character,newCharacter,ocuurence)
            return newValue
        except:
            print("exception occured enter string input")
        
    def concat(self,value1,value2)-> str:
        try:
            value3 = str(value1) + str(value2)
            return value3
        except:
            print("Check your input")
            

val = strings()
#print(val.removeChar('Hello','l','o'))
print(val.concat('Hel','lo'))