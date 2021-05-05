# check whether an integer is a prime number or not using for loop and if...else statement

not_prime = False
num = 29
if num > 1:
  # check for factors
  for i in range(2, num):
    if num (num % i) == 0:
      # if factor is found
      not_prime = True
        
if not_prime:
  print(num, "is not a prime")
 else:
  print(num, "is a prime")
  
# ---------------------------------------------------------------------------------------
  
if num > 1:
  for i in range(2, num):
    if (num % i) == 0:
      print(i,"x",num//i,"=",num)
  else:
    print(num, "is a prime number")
else:
  print(num, "is not a prime number")
  
  
# -------------------------------------------------------------------------------------------

# print all prime numbers in an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      print(num)
