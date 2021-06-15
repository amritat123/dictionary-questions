dict_1={}
i=1
user=int(input("enter number"))
while i<=user:
    j=1
    list_1=[]
    while j<=10:
        a=j*i
        list_1.append(a)
        j+=1
    dict_1[i]=list_1
    i+=1
print(dict_1)

