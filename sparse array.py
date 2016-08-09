with open('sparse_array.txt') as f:
    content = f.readlines()

n = int(content[0])

strings = {}
for _ in range(n):
    inpt = content[_]
    if inpt in strings:
        strings[inpt] += 1
    else:
        strings[inpt] = 0

q = int(content[5])
for _ in range(q):
    query = content[_]
    if query in strings:
        print strings[query]
    else:
        print 0
