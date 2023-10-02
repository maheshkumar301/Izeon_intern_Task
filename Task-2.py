signal=['green','yellow','green','green','black','red','green','yellow','yellow','red','red','black']
a=[]
for i in signal:
    if i=='green':
        a+=['go']
    elif i=='yellow':
        a+=['ready']
    elif i=='red':
        a+=['stop']
    else:
        continue
        
print(signal)
print(a)
