#This program counts seconds for you, it's like a stopwatch. And it also asks you your name, just to make it cool, thanks!

import time
N = str(input("What´s your name? "))
T = int(input(f"Welcome {N}, how long you want to wait? "))

for i in range(T, 0, -1):
    print(i)
    time.sleep(1)

print(f"Ready! See you {N}!")
