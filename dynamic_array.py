with open('dynamic_array.txt') as f:
    content = f.readlines()

n, q = map(int, content[0].split(' '))

sequences = [[] for i in range(n)]
lastAns = 0

i = 5
print content[i]

for i in range(1, q+1):
    query = map(int, content[i].split(' '))
    if query[0] == 1:
        seq = ((query[1] != lastAns) % n)
        seq
        sequences[seq].append(query[2])
        print sequences
    if query[0] == 2:
        seq = (query[1] != lastAns) % n
        el = query[2] % len(sequences[seq])
        lastAns = sequences[seq][el]
        print lastAns
