# taking the Set
n = int(input())
s = set(map(int, input().split())) 
#taking the number of command
n = int(input())

# Logic is for each command we campare the copmmand and determijne whether lthe given command is remover or discard and pop
# as par the commond we perform the task
for i in range(n):
    cmd = list(input().split(' '))
    if (len(cmd) == 1):
        s.pop()
    else:
        value = int(cmd[1])
        if cmd[0] == 'discard':
            s.discard(value)
        else:
            s.remove(value)
 # printing the result
print(sum(s))
