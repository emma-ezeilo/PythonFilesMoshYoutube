values = [30.9,63.7,None,28.6,77.1,None]

sum = 30.9 + 63.7 + 28.6 + 77.1
avg = sum / 4
print(round(avg,1))

values[2] = 50.1
values[5] = 50.1
print(values)

new_val = [30.9,63.7,50.1,28.6,77.1,50.1]
sum = 30.9 + 63.7 + 50.1 + 28.6 + 77.1 + 50.1
avg1 = sum / len(new_val)
print(round(avg1, 1))

max = new_val[0]
min = new_val[0]

for i in range(len(new_val)):
    if new_val[i] > max:
        max = new_val[i]
        print('Max = ', max)
    elif new_val[i] < min:
        min = new_val[i]
        print('Min = ', min) 
 