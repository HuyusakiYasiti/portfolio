import random

import time


n = input("Please enter an integer value.: ")

n = int(n)


for i in range(n, 0, -1):

    print(i)

    time.sleep(random.triangular(0.5, 1.5, 1.0))

print("complete")
