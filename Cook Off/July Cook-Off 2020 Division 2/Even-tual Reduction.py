# Problem Statement Link : https://www.codechef.com/COOK120B/problems/EVENTUAL

for _ in range(int(input())):
    n = int(input())
    arr = list(input())
    alpha = {}
    for each in arr:
        alpha[each] = 0
    for each in arr:
        alpha[each] += 1
    ans = "YES"
    for each in alpha.values():
        if each % 2 != 0:
            ans = "NO"
    print(ans)
