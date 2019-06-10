arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 
arr.sort()
dep.sort()
print(arr)
print(dep)
count=1
count1=1
i=1
for i in range(n):
    
    j=i-1
    if(arr[i]<=dep[j]):
        count=count+1

        if(count>count1):
            count1=count
    else:
        count=count-1
        j=j+1
print("Minimum No Of Platforms Required will be :- ",count1)
