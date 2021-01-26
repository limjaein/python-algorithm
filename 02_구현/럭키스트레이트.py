score = input()
half = int(len(score)/2)
left = 0
right = 0

for idx in range(0, half):
    left += int(score[idx])
    right += int(score[-(idx+1)])

if left == right:
    print("LUCKY")
else:
    print("READY")