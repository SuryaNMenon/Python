sum = 0
n = int(input('Enter range'))
for i in range(0,n+1):
    if i%2 == 0:
         continue
    else:
         sum = sum+i
print(sum)
