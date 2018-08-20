for _ in range(int(input())):
    try:
        a,b=list(map(int,input().strip().split()))
        try:
            c=int(a/b)
            print(c)
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
