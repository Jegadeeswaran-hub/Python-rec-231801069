#Program:
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
distinct_elements = set(arr)
print(*distinct_elements)
