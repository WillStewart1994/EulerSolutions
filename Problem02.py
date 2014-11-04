x = 1
y = 0
temp = 0
sum = 0
n = 0;

while x < 4000000:
    temp = x
    x += y
    y = temp
    if x%2 == 0:
        sum+=x

print(sum)