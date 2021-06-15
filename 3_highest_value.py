my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
max=0
list1=[]
for i in  my_dict.values():
    if i>max:
        max=i
        list1.append(max)
print(list1)
