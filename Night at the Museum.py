s = input()

total_rotations = 0
current_pos = 0

for char in s:
    target_pos = ord(char) - ord('a')
    diff = abs(target_pos - current_pos)
    total_rotations += min(diff, 26 - diff)
    current_pos = target_pos

print(total_rotations)
