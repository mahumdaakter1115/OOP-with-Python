from collections import Counter

# Read input
N = int(input())
a = list(map(int, input().split()))

# Count the occurrences of each element
count = Counter(a)

# Calculate the minimum number of elements to be removed
removals = 0
for x in count:
    if count[x] > x:
        removals += count[x] - x

# Print the result
print(removals)
