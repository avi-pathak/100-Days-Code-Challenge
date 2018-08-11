A  = set(input().split())  # taking the input main Array
n = int(input())   #taking the number of the lemnt in the next two array
check = True      # intialy we assume that it is the super set
for i in range(n):
    s = set(input().split())
    '''# this is the main line here we checkin if the content of second array is not equal to array A and also the inetersection of
    s and  are not equal the we make check to false and break the loop'''
    if (s&A != s) or (s == A): 
        check = False
        break
print(check)
