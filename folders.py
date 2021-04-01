# The paths to files and directories are specified in the form of names separated by a slash
# for example "a/b/c" , "b/d" , "test".
# print them in the form of a tree with children arranged lexicographically.

# INPUT
# The first line contains integer n (1 <= n <= 100) , the number of paths
# Next n lines contain the paths themselves, one per line
# all paths are different, consist of small Latin letters and slashes, have lengths fom 1 to 100
# no path starts with a slash, ends with a slash, or contains two or more slashes in a row

# OUTPUT
# print the folder tree as requested

num_paths = int(input())

paths = []

for i in range(num_paths):
    path = input()
    paths.append(path)

lst = []

for path in paths:
    lst.append(path.split("/"))

print(lst)

dct_paths = {}

for path in lst:
    idx = 0
    dct = dct_paths
    while idx < len(path):

        if path[idx] not in dct.keys():
            dct[path[idx]] = {}

        dct = dct[path[idx]]
        idx = idx + 1

print(dct_paths)

def traverse_dct(dct, level):
    for key in sorted(dct.keys()):
        print("+"*level+key)
        traverse_dct(dct[key], level+1)

traverse_dct(dct_paths,0)

        
