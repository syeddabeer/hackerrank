#Numbers ending in 3 have at least one multiple having all ones

import numpy as np

count = 1
rem = 1
n=3 #input("enter a number ending in 3:")

while rem:
	rem = (rem*10 + 1)%n
	count += 1
	print(f"count is {count}")

output=0
for i in range(0, count, 1):
	output += np.power(10, i)
	print(f"output is {output}")

print(output) 

