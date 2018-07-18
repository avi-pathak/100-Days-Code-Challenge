b=4
for x in range(b):
        for y in range(b-x):
                print(" -",end='')
        print(" *"*(b+x+x),end='')
        for y in range(b-x):
                print(" -"*2,end='')
        print(" *"*(b+x+x),end='')
        print()

print(" *"*(4*6))
k=22
for x in range(b*3):
        for x in range(x+1):
                print("  ",end='')
        print(" *"*k if k > 0 else "*")
        
        k-=2
