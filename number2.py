from collections import Counter

def minimum_removals(N, a):
    count = Counter(a) 
    removals = 0

    for x in count:
        if count[x] > x:
            removals += count[x] - x

    return removals
N = int(input())
a = list(map(int, input().split()))
print(minimum_removals(N, a))
