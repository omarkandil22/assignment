prime = [1] * 500000
prime[0] = 0

for i in range(3, 1000, 2):
    if prime[i // 2]:
        prime[(i * i) // 2::i] = [0] * len(prime[(i * i) // 2::i])

print("Input the number(n):")
n = int(input())
if n < 4:
    print("Number of prime numbers which are less than or equal to n.:", n - 1)
else:
    print("Number of prime numbers which are less than or equal to n.:", sum(prime[:(n + 1) // 2]) + 1)
