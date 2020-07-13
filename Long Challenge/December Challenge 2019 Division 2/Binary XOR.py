# 5 Problem Statement Link : https://www.codechef.com/DEC19B/problems/BINXOR

# Solution :

N = 1000001

factorialNumInverse = [None] * (N + 1)

naturalNumInverse = [None] * (N + 1)

fact = [None] * (N + 1)


def InverseofNumber(p):
	naturalNumInverse[0] = naturalNumInverse[1] = 1
	for i in range(2, N + 1, 1):
		naturalNumInverse[i] = (naturalNumInverse[p % i] *
		                        (p - int(p / i)) % p)


def InverseofFactorial(p):
	factorialNumInverse[0] = factorialNumInverse[1] = 1

	for i in range(2, N + 1, 1):
		factorialNumInverse[i] = (naturalNumInverse[i] *
		                          factorialNumInverse[i - 1]) % p


def factorial(p):
	fact[0] = 1

	for i in range(1, N + 1):
		fact[i] = (fact[i - 1] * i) % p


def Binomial(N, R, p):
	ans = ((fact[N] * factorialNumInverse[R]) % p *
	       factorialNumInverse[N - R]) % p
	return ans


p = 1000000007
InverseofNumber(p)
InverseofFactorial(p)
factorial(p)

for _ in range(int(input())):
	m = int(input())
	A = input()
	B = input()
	A_ones = A.count('1')
	B_ones = B.count('1')
	min_ones = abs(A_ones - B_ones)
	if (A_ones + B_ones) >= m:
		max_ones = (2 * m) - (A_ones + B_ones)
	else:
		max_ones = A_ones + B_ones
	sum_ = 0
	# value = math.factorial(m)
	while min_ones <= max_ones:
		# sum_ += (value//(math.factorial(min_ones)*math.factorial(m-min_ones)))
		# sum_ +=(dp[m])//(dp[min_ones]*dp[m-min_ones])
		sum_ += Binomial(m, min_ones, p) % p
		min_ones += 2
	print(sum_ % p)
