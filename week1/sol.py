file = 'D:\\GitHub\\learning_python\\stepik_learning_python_01\week1\\dataset_3380_5.txt'

with open(file, 'r') as f:
    text = f.read()

d = {}

for row in text.splitlines():
    level, name, height = row.split('\t')
    level = int(level)
    height = int(height)
    if level in d:
        d[level].update({name: height})
    else:
        d[level] = {name: height}


for i in range(1, 12):
    s = 0
    if i not in d.keys():
        print(f'{i} -')
    else:
        if len(d[i].values()) == 1:
            print(f'{i}', end=" ")
            for val in d[i].values():
                print(float(val))
        else:
            for v in d[i].values():
                 s += v
            s_height = s / len(d[i].values())
            print(f'{i} {float(s_height)}')

