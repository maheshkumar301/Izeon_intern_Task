inp=input("Enter a string:")
inp=inp.lower()
inp=" ".join(inp)
inp=inp.split()
count=0
for i in inp:
    if i in ['a','e','i','o','u']:
        count+=1

print(count)



