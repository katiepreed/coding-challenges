# there are currently n packages for delivery in the mail office. 
# the weight of each package is either 50 kg or 100 kg
# it is known that no more than 150 kg can be transported bt car in one trip

# what is the smallest number of courier trips needed to deliver all the packages
# parcels must not be deivered in any other way than by courier. 

# INPUT
# the first line of the input contains an integer n(1 <= n <= 1000), the number of packages. 
# The second line contains the wights of the packages (each number is either 50 or 100). 

# OUPUT 
# Print a single integer, the smallest number of courier trips, if in one trip he can deliver no more than 150 kg of cargo. 

packages = int(input())
weights = input()
weight = weights.split(" ")

hun = 0
fif = 0
num = len(weight)

for i in range(num):
    if weight[i] == "100":
        hun = hun + 1
    elif weight[i] = "50":
        fif = fif+1

if hun >= fif:
    count = hun - fif
    trip = int(fif+count)
    print(trip)

if hun<fif:
    count = fif-hun

    if count % 3 = 0:
        count1 = count / 3
    else:
        count1 = (count //3) + 1

    trip = int(hun + count1)
    print(trip)
