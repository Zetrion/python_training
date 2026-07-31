def findPlatform(arr, dep):
    
    arr.sort()
    dep.sort()
    
   
    plat_needed = 0
    result = 0
    
 
    a = 0
    d = 0
    n = len(arr)
    
    
    while a < n and d < n:
        
        if arr[a] <= dep[d]:
            plat_needed += 1
            a += 1
        
        else:
            plat_needed -= 1
            d += 1
            
       
        if plat_needed > result:
            result = plat_needed
            
    return result


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1120, 1150, 1200, 1900, 2000]

print("Minimum number of platforms required:", findPlatform(arr, dep))
