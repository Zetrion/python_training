



def replace(string, old, new):  
    
    if old not in string:
        return string  
    
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new  
            i += len(old)  
        else:
            result += string[i]  
            i += 1  

    return result  

print(replace(input("Enter a string: "), input("Enter the substring to replace: "), input("Enter the new substring: "))) 
