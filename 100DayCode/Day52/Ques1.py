''just simple problem we need split the string according to "," and "." for that regex are the best choice'''
import re
[print(i) for i in re.split("[,\.]?",input().strip()) if i]
