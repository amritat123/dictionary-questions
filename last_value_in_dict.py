import json

my_dict={"key1": "value1", "key2": "value2"}
j=0
for i in my_dict.keys():
    if j==len(my_dict)-1:
        print(my_dict[i])
    j+=1


   
