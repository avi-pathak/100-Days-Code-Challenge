while True:
     l=list(input().split())
     if(len(l) == 1):
          break
     else:
          x1,y1,x2,y2,p=float(l[0]),float(l[1]),float(l[2]),float(l[3]),float(l[4])
          k=(x1-x2)
          k=k*-1 if k<0 else k
          l=y1-y2
          l=l*-1 if l<0 else k
          res1=k**p
          res2=l**p
          final_result = res1 + res2
          k=1/p
          output=final_result**k
          output=output*-1 if output<0 else output
          print("%.10f"%(output))
          
