# n =  int(input())
# li=[]
# for i in range(n+1):
#     li.append(0)
# for i in range(1,n+1):
#         for j in range(1,n+1):
#             if(j%i==0):
#                 if(li[j]==1):
#                     li[j]=0
#                 elif(li[j]==0):
#                        li[j]=1
#         print(li)                   
# c=li.count(1)
# print(c)
x=list(map(int,input("").split()))
d=0
for i in x:
    x.remove(i)
    c=x.count(i)
    if c>0:
        d=d+c
    for j in range(c):
        x.remove(i)
print(d)      
    