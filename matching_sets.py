# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = 4#int(raw_input())
x = [0,2,0,2]#map(long, raw_input().split(' '))
y = [1,1,1,1]#map(long, raw_input().split(' '))

# In each counter I check how many times a value is repeated in an array
cnt_x = Counter()
for e in x:
    cnt_x[e] += 1

cnt_y = Counter()
for e in y:
    cnt_y[e] += 1

# In extra_values is stored the values that cannot be deleted because not
# equal in the two arrays
extra_values = {}

for key in cnt_x.keys:
    if key is in cnt_y:
        extra = cnt_x[key] - cnt_y[key]
        if extra != 0:
            extra_values[key] = difference
    else:
        #se non ci sono da una parte o dall'altra vanno aggiunti comunque

for i in range(n):
    if x[i] != y[i]:
        diff.append(x[i] - y[i])

if sum(diff) == 0:
    pos_diff = sum([e for e in diff if e > 0])
    neg_diff = sum([e for e in diff if e < 0])
    assert pos_diff == abs(pos_diff)
    print pos_diff
else:
    print -1
