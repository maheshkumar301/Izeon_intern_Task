#list to dictionary
l=['1234','raju','3456','riya','6789','joe']
l1=l[::2]
l2=l[1::2]
l=zip(l1,l2)
print(dict(l))
