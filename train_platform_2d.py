trains = [[0,5], [1,2], [1,10], [3,4], [5,6], [7,8]]

arr = sorted( [train[0] for train in trains])
dep = sorted([train[1] for train in trains])

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




print("Minimum number of platforms required:", findPlatform(arr, dep))
