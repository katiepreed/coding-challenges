# given a string s consisting of sentences. Each sentence consists of English letters only
# and ends with a single dot "." or three dots "..." 
# given a string of letters and dots. Find thr k-th sentence. 

# INPUT
# The first line contains integer k, the number of the sentence to be displayed. 
# The second line contains the string s, consisting of letters and dots. The string length does not exceed 10^5 characters. 

# It is guaranteed that the given string is a sequence of at least k sentences. 
# It is guaranteed that each sentence consists of english letters only, contains at least one letter and ends with a single dot or three dots. 

# OUPUT
# print the k-th sentence along with the ending punctuatuon mark. 

K = int(input())
sen = []
word = []
newarray = []
sentence = input()
array = sentence.split(".")

for i in range(len(array) - 1):
    newArray.append(array[i])

newArray.append("extra")
#newArray.append("extra")

num = len(newArray)

for i in range(num-2):
    if new_array[i] != "" and newArray[i+1] != "":
        sen.append(newArray[i]+".")
    elif newArray[i] != "" and newArray[i+1] == "":
        sen.append(newArray[i]+".")

print(sen[K-1])