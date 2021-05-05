# Palindrome is defined as a word, phrase, number or other sequence of charactres which reads the same backwards as forwards

# find if a string is Palindrome or not
# Find if a number is Palindrome or not

def palindrome(word):
    lst = list(str(word))
    reverse =  []

    num = len(lst)

    for i in range(num):
        reverse.append(lst[-(i+1)])
        
    print("word: ", lst)
    print("reverse: ", reverse)

    if reverse == list(str(word)):
        print("palindrome")
    else:
        print("not palindrome")

palindrome(12321)
