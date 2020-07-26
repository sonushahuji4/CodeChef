# Problem Statement Link : https://www.codechef.com/LTIME86B/problems/CHEFSTEP

# Implementation :
for _ in range(int(input())):
    n,k = map(int,input().split())
    distance = list(map(int,input().split()))
    ans=""
    for each in distance:
        if each%k==0:
            ans+="1"
        else:
            ans+="0"
    print(ans)