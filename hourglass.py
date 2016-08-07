with open('hourglass1.txt') as f:
    content = f.readlines()


arr = []
for i in xrange(6):
    arr_temp = map(int, content[i].strip().split(' '))
    arr.append(arr_temp)

res = None
for j in range(0, 4):
    for i in range(0, 4):
        temp_res = arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+1][i+1] + \
            arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]
        if temp_res > res:
            res = temp_res
print res
