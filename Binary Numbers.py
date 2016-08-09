n = bin(439)
n = list(n[2:])
n = map(int, n)

# now n is a list of 0s and 1s
max1 = 0
tmp = 0
for i in range(len(n)):
    if n[i] == 1:
        tmp += 1
    if n[i] == 0 or i == len(n)-1:
        if tmp > max1:
            max1 = tmp
        tmp = 0
max1
