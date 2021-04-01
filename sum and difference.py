# Peter and Paul found two integer numbers x and y. 
# Peter remembers the sum of these numbers a = x + y
# and paul remebers their difference b = x - y
# help them restore the original numbers x and y by given numbers a and b

# INPUT
# The only input line contains two integers a and b (-10^9 <= a <= 10^9 , -10^9 <= b <= 10^9). 
# It is guaranteed that for given numbers a and b, the corresponding x and y integers. 

# OUTPUT
# output two integers x and y

a,b = map(int, input().split())
sum = a + b
x = int(sum/2)
y = int(a-x)
print(x,y)
