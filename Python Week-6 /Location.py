#Program:
n = int(input())
arr = [int(input()) for _ in range(n)]
element_to_search = int(input())
locations = []
occurrences = 0
for i in range(len(arr)):
    if arr[i] == element_to_search:
        locations.append(i + 1)
        occurrences +=1
if occurrences == 0:
    print(f"{element_to_search} is not present in the array.")
else:  
    for loc in locations:
        print(f"{element_to_search} is present at location {loc}.")
    print(f"{element_to_search} is present {occurrences} times in the array.")
