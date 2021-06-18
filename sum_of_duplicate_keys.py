dict1={"a":5,"b":7,"c":10,"d":5}
dict2={"c":10,"r":5,"d":10,"a":25}
my_dict={}
for i in dict1:
    for j in dict2:
        if i==j:
            my_dict[i]=dict1[i]+dict2[j]
        else:
            my_dict[i]=dict1[i]
print(my_dict)


