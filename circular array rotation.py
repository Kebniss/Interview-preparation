with open("rotation.txt") as f:
    content = f.readlines()

n, k, q = map(int,  content[0].split(' '))
array = map(int, content[1].split(' '))

if (k/n > 0):
    c = k/n
    k = k - (c*n)

x = n - k
k_rotated = list(array)

for i, val in enumerate(array):
    try:
        i_new = i-x
        k_rotated[i_new] = val
    except IndexError:
        print "i = {}, x = {}, i_new = {}".format(i,x,i_new)

for _, q in enumerate(content[2:]):
    try:
        print k_rotated[int(q)]
    except IndexError:
        print _,q
