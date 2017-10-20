def LetterCapitalize(str): 

    words=str.split(" ")
    for i in range(len(words)):
            words[i]=words[i][0].upper()+ words[i][1:]
        
    return " ".join(words)
    
# keep this function call here  
print LetterCapitalize('hello world')  
