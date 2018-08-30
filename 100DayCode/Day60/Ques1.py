def addpoly(p1,p2):
    i,j=0,0
    result=[]
    while(i<len(p1) and j<len(p2)):
        if(p1[i][1] > p2[j][1]):
            result.append(p1[i])
            i+=1
        elif p1[i][1] < p2[j][1]:
            result.append(p2[j])
            j+=1
        else:
            sum=p1[i][0] + p2[j][0]
            pow=p1[i][1]
            t=(sum,pow)
            if sum !=0:
                result.append(t)
            i+=1
            j+=1
    while i<len(p1):
        result.append(p1[i])
        i+=1
    while j<len(p1):
        result.append(p1[j])
        j+=1
    return result
