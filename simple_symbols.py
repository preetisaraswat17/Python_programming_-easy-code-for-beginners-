'''Have the function SimpleSymbols(str) take the str parameter being passed and 
determine if it is an acceptable sequence by either returning the string true or false. 
The str parameter will be composed of + and = symbols with several letters between them 
(ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. 
So the string to the left would be false. The string will not be empty and will have at least one letter. '''


def SimpleSymbols(str): 

    #pad the string first so that it does not give out of bound errors
    new_str='='+str+'='
    for i in range(0,len(new_str)):
       if new_str[i].isalpha():
           if new_str[i-1]!='+' or new_str[i+1]!='+':
            return False
    
    return True
    
# keep this function call here  
print SimpleSymbols(str)
