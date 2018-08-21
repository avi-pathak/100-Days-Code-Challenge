''' i have used regex module actuall regex stand for regular expression in that i use a simple searcg function and seach a 

certain sequance of email address'''

import re
def fun(s):
    t=re.search(r"^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$",s)# it will retrun true if all the condion matched in s 
    if t:
        return s
