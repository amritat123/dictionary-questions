my_dict = {
    'data1':100,
    'data2': -54,
    'data3': 247
} 
values=my_dict.values()
total=sum(values)
print(total)

# second method......
sum=0
for i in my_dict.values():
    total=sum+my_dict[i]
print(total)