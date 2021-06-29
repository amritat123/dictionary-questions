dict_1={"a":  1,"a":  2,"a":  3, "a": 4,"b": 1,"b": 2}
dict1={}
for i in dict_1:
        if i in dict_1:
            dict1[i]=dict_1[i]
print(dict1)