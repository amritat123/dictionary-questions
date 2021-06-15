dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.keys():
    total=0
    for j in dict1.values():
        total+=j
    sum+=i
print(total)
print(sum)