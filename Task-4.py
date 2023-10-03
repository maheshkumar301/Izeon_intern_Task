#get input in list and show output in set of prime numbers
a=int(input("Enter starting range:"))
b=int(input("Enter ending range:"))
l=list(range(a,b))
s=[]
for i in l:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s.append(i)
print(set(s))
        
