import threading as th
import time

l=Lock()
def wish(name):
    for _ in range(10):
        print("good morning ")
        time.sleep(2)
        print(name)


t = th.Thread(target = wish ,args = ("Avinash",))

t1 = th.Thread(target = wish ,args = ("ashutosh",))



t2 = time.time()
t.start()
t1.start()
t3 = time.time()
time.sleep(25)
print("time taken by thread ",t3- t2)

t2 = time.time()
wish('Avinash')
wish('Ashutosh')

print("time taken by using without thread ",time.time() - t2)
