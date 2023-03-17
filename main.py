ans = []
for a in range(1, 300):
    for x in range(1, 200):

        for y in range(1, 200):

            for z in range(1, 200):
                if not (((x | 50) == x) or ((y & 34) != 0) or ((z | 24) != 24) or (x * y * z > a // 8)):
                    break
            if not (((x | 50) == x) or ((y & 34) != 0) or ((z | 24) != 24) or (x * y * z > a // 8)):
                break
    if not (((x | 50) == x) or ((y & 34) != 0) or ((z | 24) != 24) or (x * y * z > a // 8)):
        break
else:
    ans.append(a)

print(max(a))
