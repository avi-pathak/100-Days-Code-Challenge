with open("abc.txt",'r') as f:
     l=f.read()
     max=''
     for word in l.split():
          if len(max)<len(word):
               max=word
     print(max)
