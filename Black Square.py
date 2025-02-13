a1, a2, a3, a4 = map(int, input().split())
s = input()

calories = [a1, a2, a3, a4]

total_calories = 0

for ch in s:
    total_calories += calories[int(ch) - 1]

print(total_calories)
