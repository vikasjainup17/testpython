n=int(input())
if n== 0:
    print(0)
else:
    arr=[]
    for i in range(n):
        arr.append(0)
    for i in range(n):
        arr[i] = 1
    print(arr)
    
    for i in range(1,n,2):
        arr[i]=0
    print(arr)
    
    i=2
    while i<n:
        j=i
        if j%i ==0:
            if arr[j]==1:
                arr[j]=0
            else:
                arr[j]=1
        j+=i+1
        if j>=n-1:
            print(arr)
            i+=1                            


# n =  int(input())
# li=[]
# for i in range(n+1):
#     li.append(0)
    
