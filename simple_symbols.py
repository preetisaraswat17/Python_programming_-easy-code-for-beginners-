def SimpleSymbols(str): 

    new_str='='+str+'='
    for i in range(0,len(new_str)):
       if new_str[i].isalpha():
           if new_str[i-1]!='+' or new_str[i+1]!='+':
            return False
    
    return True
    
# keep this function call here  
print SimpleSymbols('+d+=3=s+')