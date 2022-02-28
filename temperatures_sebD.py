import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
tp = 5526 # highest possible value

if int(n) > 0: 
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
 
        if abs(t) < abs(tp):   
            tp = t
        if tp+t == 0:
            tp = abs(t)

# If no value, exit with value = 0
else:
    tp = 0


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(tp)
