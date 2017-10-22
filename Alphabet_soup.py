'''Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with
 the letters in alphabetical order (ie. hello becomes ehllo). 
Assume numbers and punctuation symbols will not be included in the string. 
Use the Parameter Testing feature in the box below to test your code with different arguments.'''

def AlphabetSoup(str): 

    #remove numbers and characters using translate
    str=str.translate(None,'!@#$%^&*_+:",.0123456789')
    # split list into characters
    str=sorted(str)
    #create a new empty list 
    return "".join(str)
# keep this function call here  
print AlphabetSoup(raw_input())  