# check for anagram
def is_anagram(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
 
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)


str1 = "Listen"
str2 = "Silent"
print(is_anagram(str1, str2))  