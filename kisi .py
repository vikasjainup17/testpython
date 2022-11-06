num=int(input(""))
st=""
st2=str(num)
for i in range(len(st2)):
            d=10**(len(st2)-1-i)
           
            c=num/d
            c=c*(10**(len(st2)-1-i))
            if c==1:
                st=st+"I"
            elif c==2:
                st=st+"II"
            elif c==3:
                st=st+"III"
            elif c==4:
                st=st+"IV"
            elif c==5:
                st=st+"V"
            elif c==6:
                st=st+"VI" 
            elif c==7:
                st=st+"VII" 
            elif c==8:
                st=st+"VIII"
            elif c==9:
                st=st+"IX"
            elif c==10:
                st=st+"X"
            elif c==20:
                st=st+"XX"  
            elif c==30:
                st=st+"XXX"
            elif c==40:
                st=st+"XL"
            elif c==50:
                st=st+"L"
            elif c==60:
                st=st+"LX" 
            elif c==70:
                st=st+"LXX" 
            elif c==80:
                st=st+"LXXX"
            elif c==90:
                st=st+"XC" 
            elif c==100:
                st=st+"C" 
            elif c==200:
                st=st+"CC" 
            elif c==300:
                st=st+"CCC"
            elif c==400:
                st=st+"CD" 
            elif c==500:
                st=st+"D"
            elif c==600:
                st=st+"DC" 
            elif c==700:
                st=st+"DCC"
            elif c==800:
                st=st+"DCCC" 
            elif c==900:
                st=st+"CM" 
            elif c==1000:
                st=st+"M" 
            elif c==2000:
                st=st+"MM"  
            elif c==3000:
                st=st+"MMM" 
print(st)        