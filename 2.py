a = [2**n + 1 for n in range(1, 32) if 2**n + 1 <= 500_000_000]
ans = []
ans += a
for i in a:
    ans += [i * 2**n for n in range(1, 32) if i * 2**n <= 500_000_000]

print(len(ans))
