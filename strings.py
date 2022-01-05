class strings:

    #Remove any given character from string
    def removeChar(self,value,character,newCharacter,ocuurence=1)-> str:
        try:
            newValue = value.replace(character,newCharacter,ocuurence)
            return newValue
        except:
            print("exception occured enter string input")
        


val = strings()
print(val.removeChar('Hello','l','o'))