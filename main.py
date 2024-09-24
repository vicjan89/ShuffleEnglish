from random import shuffle


with open('lesson10.txt', 'r', encoding='utf8') as f:
    rows = f.readlines()

for i in range(1, 17):
    shuffle(rows)
    with open(f'lesson10_{i:02}.txt', 'w', encoding='utf8') as f:
        f.writelines(rows[:20])