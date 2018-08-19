'''
in this probl;em we just need to check two thing if a string contai9n a alphabetic letter then it should not be a phone Number

and if it strats with 7 8 9 and its length is 10 then it is valid phone number

SIMPLE!!!
'''
for _ in range(int(input())):
    k=input()
    if k.isdigit()==False:
        print("NO")
        continue
    if(len(k) == 10 and (k[0] == '7' or k[0] == '8' or k[0] == '9')):
        print("YES")
    else:
        print("NO")
