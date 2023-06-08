
N = int(input())
numbers = list(map(int, input().split()))
max_op = 0
while all(num % 2 == 0 for num in numbers):
    numbers = [num // 2 for num in numbers]
    
    max_op += 1

print(max_op)
