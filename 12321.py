F = [0] * 13345
for n in range(12445, 0, -1):
    if n > 10000:
        F[n] = n - 10000
    elif 1 <= n <= 10000:
        F[n] = F[n + 1] + F[n + 2]

print(F[12345] * (F[10] - F[12]) / F[11] + F[10101])