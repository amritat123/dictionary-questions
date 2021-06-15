# dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

dict1 = {1: 1, 2: 9, 3: 4}

sorted_values = sorted(dict1.values()) 
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break
print(sorted_dict)





