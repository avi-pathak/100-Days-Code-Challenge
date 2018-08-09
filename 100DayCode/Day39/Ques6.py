def merge_the_tools(s, n):
    k=''
    m=''
    for i in range(len(s)):
        if i % n == 0 and i != 0:
            if i == n:
                m+=k
            else:
                m+='\n'+k
            k=''
        if s[i] not in k:
            k+=s[i]
    m+="\n"+k
    print(m.lstrip('\n'))
