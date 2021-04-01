# a virus epidemic has swept Byteland. There are m citizens in Byteland. 
# Each of these people is either healthy or sick. 
# in order of the tests, a certain group of citizens was selcted and 
# blood was taken from each citizen of this group. The resulting material was
# was mixed and sent for analysis. As a result, if the test showed "no infection",
# it means that all citizens of the group are helthy
# otherwise (if the test showed "there is an infection"), it means that there
# is at least one sick citizen in the group. 
# Given the information about the tests, you need to find out the status of each citizen: 
# healthy, sick or unknwown


# INPUT
# The first line contains two numbers n and m: the number of testing groups
# (1 =< n =< 1000) and the total number of citizens (1 =< m =< 1000)
# the following n lines contain the description of tests
# Each description starts with a pair of numbers ai , ki, (0 =< ai =< 1, 1 =< ki =< m)
# the result of the test of the group (if ai = 0, then the test result is "no ifection")
# (if ai = 1, then the test result is "there is an ifection")
# and the number of citizens in the tested group. 
# next in line there are k, distinct integers bij, the numbers of the citizens
# tested in this group (1 =< bij =< m)
# consider citizens numbered from 1 to m. 
# All nubers in the input are integers. It is guaranteed that the input is consistent. 

# OUTPUT
# print m integers: the status for each citizen from 1 to m. 
# The number should be 0 for "healthy" , 1 for "sick" or 2 for "unknown". 

n,m = input().split

n = int(n)
m = int(m)

result = []
for i in range(n):
    test  = input().split()
    test = [int(elem) for elem in test]
    results.append(test)

# 2 - unknown
# 1 - infected
# 0 - nor infected

citizen_status = []

for i in range(m):
    citizen_status.append(2)

for test in result:
    if test[0] = 0:
        group_size = test[1]
        for i in range(group_size):
            person_id = test[i+2]
            citizen_status[person_id - 1] = 0

unhealthy_groups = []
for test in results:
    if test[0] == 1:
        # group_size = test[1]
        group = test[2:]
        new_group = []

        for person_id in group:
            if citizen_status[person_id - 1] != 0:
                new_group.append(person_id)

        unhealthy_groups.append(new_group)

# unhealthy_groups is the list of groups of people which are potentially infected

for group in unhealthy_groups:
    if len(group) == 1:
        person_id = group[0]
        citizen_status[person_id - 1] = 1