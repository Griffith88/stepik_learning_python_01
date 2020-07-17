objects = [1, 2, 1, 2, 3]
ans = 0
i = 0

for obj in objects:
    if not obj is objects[i + 1]:
        i += 1
        ans += 1
    else:
        i += 1
print(ans)
