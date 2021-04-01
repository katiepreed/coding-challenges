# On the bytesbury tube line each passenger is issued with a ticket that has a unique number.
# these numbers are integers and are ussued in order such that after the ticket numbered x, the next
# ticket will have the numbers x + 1
# peter says the ticket is lucky if the sum of the digits in even positions is equal to the sum of the
# digits in odd positions
# peter knows the most reecent ticket issued has the number n. He wonders when the nect lucky ticket
# will be issued. Help him find the minimal ticket number, greater than n, that is lucky number.
# Please note that the number n may be huge.

# INPUT
# Input contains one integer number n(1 <= n <= 10^100)

# OUTPUT
# Print one integr, the minimal ticket number, greater than n, that is a lucky number

n = list("0" + input())

def solve(n):
    even_sum = sum(map(int,n[::2]))
    odd_sum = sum(map(int,n[1::2]))

    for i in range(len(n) -1, -1, -1):
        parity = (i+1) % 2
        for j in range(i + 1, len(n)):
            if parity:
                odd_sum -= int(n[j])
            else:
                even_sum -= int(n[j])

            parity = not parity
            n[j] = "0"

        if n[i] == "9":
            continue

        n[i] = str(int(n[i]) + 1)

        if i % 2 == 0:
            even_sum += 1
        else:
            odd_sum += 1

        if odd_sum == even_sum:
            break

        if even_sum < odd_sum:
            for j in reversed(range(i + (i % 2 == 1), len(n), 2)):
                nval = max(int(n[j]), min(9, int(n[j]) + odd_num - even_sum)):
                even_sum += nval - int(n[j])
                n[j] = str(nval)
                
        elif odd_sum < even_sum:
            for j in reversed(range(i + (i % 2 == 0), len(n), 2)):
                nval = max(int(n[j]), min(9, int(n[j]) + even_sum - odd_sum))
                odd_sum += nval - int(n[j])
                n[j] = str(nval)


        if odd_sum == even_sum:
            break

    return int("".join(n))

print(solve(n))
