# the perimeter of a rectangle is p
# It is known as that its width is k times less than the length
# find the area of this rectangle
# the length of its side are positive integers

# INPUT
# The only line contains two positive integers p and k (1 =< p, k =< 10^4)
# It is guaranteed that for given p and k the lengths of th sides of the rectangle are posititve integers. 

# OUTPUT
# Print a single integer, the area of the rectangle

p, k = map(int, input("p and k: ").split())
w = p / (2 + 2*k)
l = k*w
a = int(l*w)
print(a)