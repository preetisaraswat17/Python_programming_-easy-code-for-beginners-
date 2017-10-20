'''Using the Python language, have the function TimeConvert(num) take the num parameter being passed and 
return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
 Separate the number of hours and minutes with a colon.'''

def TimeConvert(num): 

    if num<60:
        minute='0:'+str(num)
        return (minute)
    else:
        hour=num/60
        minute=num%60
        time=str(hour)+':'+str(minute)
        return time
    
# keep this function call here  
print TimeConvert(126)  
















   