T=int(input(""))

p1=[]

for i in range(T):
    t=[]
    M=int(input(""))
    N=int(input(""))
    P=int(input(""))
    for j in range(N):
        tj=[]
    for j in range(N):
        for k in range(M):
            aa=int(input(""))
            tj.append(aa)
    for j in range(N):
        if tj[P-1]==max(tj):
            t.append(0)
        else:
            
            t.append(max(tj)-tj[P-1])    
        print(t)               
    p1.append(sum(t)) 
     
for i in p1:
    print(i)    
    