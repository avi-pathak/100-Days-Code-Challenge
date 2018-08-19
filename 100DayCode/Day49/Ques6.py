cube = lambda x: (x*x*x)# complete the lambda function 

def fibonacci(n):
    l=[0,1]
    first=0
    second=1
    n-=2
    for x in range(n):
        third=first+second
        l.append(third)
        first=second
        second=third
    return l
    # return a list of fibonacci numbers
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
