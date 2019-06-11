#code
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# How many elements each 
# list should have 
final_list=[]
T=int(input("Enter No of TestCases"))
for i in range(T):
    N=int(input("Enter Size of Array"))
    var=[]
    for i in range(N):
        var.append(int(input()))
    print(var)
    var.sort()
    M=int(input("Enter No of Choclates"))
    R=N-M
    final_list=list(divide_chunks(var,M))
    print(final_list)
    
    result=max(final_list[0])-min(final_list[0])
    print(result)

