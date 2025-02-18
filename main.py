from random import shuffle


with open('lesson07.txt', 'r', encoding='utf8') as f:
    rows = f.readlines()
    task = rows[0]
    rows = rows[1:]

for i in range(1, 16):
    shuffle(rows)
    rows_numbered = [f'{num+1}. {row}' for num, row in enumerate(rows[:20])]
    with open(f'lesson07_{i:02}.txt', 'w', encoding='utf8') as f:
        f.write(task)
        f.writelines(rows_numbered)