my_dict={"first":"1", "second": "2", "third": "1", "four": "5", "five":"5", "six":"9","seven":"7"}
l=[]
for i in my_dict.values():
    if i  not in l:
        l.append(i)
print(l)
    


    
    
    