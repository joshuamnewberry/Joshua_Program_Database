import time
import math

# Define variables
n = 10000 # Anything larger and n^2 takes way too long that I never got a full test to print
i1 = i2 = i3 = 0
j1 = math.log(n)
j2 = n
j3 = math.pow(n, 2)

# Time test 1
start_time1 = time.time()
while i1 < j1: # i iterates from 0 to (log2N)-1
    i1 += 1
end_time1 = time.time()
print(f"Time used for O(logn): {end_time1 - start_time1}")

# Time test 2
start_time2 = time.time()
while i2 < j2: # i iterates from 0 to N-1
    i2 += 1
end_time2 = time.time()
print(f"Time used for O(n): {end_time2 - start_time2}")

# Time test 3
start_time3 = time.time()
while i3 < j3: # i iterates from 0 to N^2
    i3 += 1
end_time3 = time.time()
print(f"Time used for O(n^2): {end_time3 - start_time3}")