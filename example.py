a = '9234'
b = '2385'
if len(a) == len(b):
    sum = '0' * len(a)
    i = len(a) - 1
    if (int(a[i]) + int(b[i])) < 10:
        k = sum[i]
        sum = sum[:i] + str(int(k) + int(a[i]) + int(b[i]))
        print(sum)
    else:
        k = sum[i - 1]
        sum = sum[:i - 1] + str(int(k) + 1) + str((int(a[i]) + int(b[i])) % 10)
        print(sum)
    for i in range(len(a) - 2, 0, -1):
        if (int(a[i]) + int(b[i])) < 10:
            k = sum[i]
            sum = sum[:i] + str(int(k) + int(a[i]) + int(b[i])) + sum[i + 1:]
            print(sum)
        else:
            k = sum[i - 1]
            sum = sum[:i - 1] + str(int(k) + 1) + str((int(a[i]) + int(b[i])) % 10) + sum[i + 1:]
            print(sum)
