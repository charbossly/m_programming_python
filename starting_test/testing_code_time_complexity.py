#get time of code execution

#import time library
import time

#start time
start_time = time.time()

for i in range(100):
    print(i)

time = time.time()-start_time
print('time of execution is',time)