with open("abc.txt",'r') as f:
     l1=f.read()
     l=[]
     for line in l1.split('\n'):
          l.append(line)
     print(l)
