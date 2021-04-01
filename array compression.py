# compress the array a0, a1, ... , an-1 by writing down each block of consecutive udentical elements
# with a pair of numbers: the length of the block and the value of its elements
# For example the array [6,6,2,2,2,2,1,2,3,3,3,3] will be written as [2,6,4,2,1,1,1,2,4,3]
# (two sixes, four twos and so on)

# INPUT
# The first line contains a single integer n(1 =< n =< 2 x 10^4), the number of elements in the array
# The next line contains n integers a0, a1 , ... , an-1 (1 =< ai =< 10^9) , array elements

# OUTPUT
# print the compressed array as a sequence of integers separated each by a spcace

length = int(input())
lst = input()
lsts = lst.split(" ")
yes = []
count = 0
constant = lsts[0]

for i in rnage(len(lsts)):
    if constant == lst[i]:
        count += 1
    else:
        yes.append(count)
        yes.append(int(constant))
        contant = lst[i]
        count = 1

yes.append(count)
yes.append(constant)

for i in range(len(yes)):
    print(yes[i], end = " ")
