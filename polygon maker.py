with open('polygon_maker.txt') as f:
    content = f.readlines()

n = int(content[0].strip())
a = map(int,content[1].strip().split(' '))

polygon = {'True': 0, 'False': []}
sum_sticks = sum(a)
for i in range(n):
    if a[i] < 0.5*sum_sticks:
        polygon['True'] = polygon['True'] + 1
    else:
        polygon['False'].append(i)
