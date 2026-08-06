

def removeDuplicates(self, s: str) -> str:
        chars = list(s)
        i = 0
        while i < len(chars) - 1:
            if chars[i] == chars[i + 1]:
                del chars[i:i + 2]         
                i = max(0, i - 1)
            else:
                i += 1              
        return "".join(chars)
    
   