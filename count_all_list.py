dict = {'T1': ['eggs', 'bacon', 'sausage'], 'T2': ['bread', 'butter', 'tosti']}

total = 0

for value in dict:
    value_list = dict[value]
    count = len(value_list)
    total += count

print(total)