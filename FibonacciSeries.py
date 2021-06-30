N = int(input('Enter the number of elements : '))
a = 0
b = 1

for i in range(0,N):
    if i<=1:
        next = i
    else:
        next = a + b
        a = b
        b = next
    print(next)
