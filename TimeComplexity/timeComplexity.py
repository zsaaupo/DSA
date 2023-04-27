"""
時間 Complexity of sum of n numbers program
"""
print(__doc__)

n = int(input("inter a interger value: "))

# 一番
sum0 = 0
LoopCount = 0
for i in range(1, n+1):
    sum0 += i
    LoopCount += 1

print("sum of", n, "is", sum0, "and loop count is", LoopCount, "so time complexity of 1st program is O(n)[order of N]")

# 二番

sum1 = int(n*(n+1)/2)
if sum1:
    OperationCount = 1

print("sum of", n, "is", sum1, "and oparation count is", OperationCount, "so time complexity of 2st program is O(1)[order of 1]")