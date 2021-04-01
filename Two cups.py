# you have two cups. Each cup holds exctly 150 ml of water. There are a ml of water (0=, a =< 150) int the first cup
# and b ml of water (0 =< b =< 150) in the seconf cup

# you want the total amount of water in both cups to be equal c ml (a+b < c =< 300)
# your task is to find out how much water to add to each cup. 
# remember that each vup cannot hold more than 150 mlpygame.examples.mask.main()

# INPUT
# The only input line contains 3 integers, a, b, c (0 =< a, b =< 150, a + b =< c =< 300)

# OUTPUT
# Print two integers, the amount of water to be added to each of the cups
# If there are severa; possible solutions, print any of them

import math
a,b,c = map(int, input("a, b, c: ").split())

water = c - (a+b)
num = water / 2

if water % 2 != 0:
    print(math.floor(num), math.ceil(num))
else:
    prin(int(num),int(num))
