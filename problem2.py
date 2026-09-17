n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

i = j = carry = 0
res = []

while i < n or j < m or carry:
    x = a[i] if i < n else 0
    y = b[j] if j < m else 0

    total = x + y + carry
    res.append(total % 10)
    carry = total // 10

    i += 1
    j += 1

print(*res)