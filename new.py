a = [1,2,3,4,6,7,99,88,999]
max_num = 0
for i in a:
    if i > max_num:
        max_num = i
print(max_num)

xy = [50, 2, 34, 6, 4, 3, 1, 5, 2] 
t=0
for i in range(len(xy)):
    if xy[i]<xy[t]:
        t=i
print t