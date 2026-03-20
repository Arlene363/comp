import random

rolls=20
sixth_roll=0
for roll in range(1,rolls+1):
    dice=random.randint(1,6)
    print(f"Roll {roll}: {dice}")
    if dice==6:
        sixth_roll+=1
print(f"Number of times a 6 was rolled: {sixth_roll}")