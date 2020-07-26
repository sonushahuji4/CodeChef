# Problem Statement Link : https://www.codechef.com/LTIME86B/problems/CHECHOC

# Implementation :

for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    ans = 0
    if (n * m == 1):
        ans = x
    elif (x * 2 <= y):
        ans = n * m * x
    elif (y >= x):
        if ((n * m) % 2 == 0):
            x = 0
        ans = ((n * m) // 2) * y + x
    else:
        ans = ((n * m + 1) // 2) * y
    print(ans)
