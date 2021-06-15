l1=[]
l2=[]
dic={}
i=0
while i<=10:
    st=input("enter the name=")
    mr=int(input("enter marks"))
    l1.append(st)
    l2.append(mr)
    i+=1
j=0
while j<len(l1):
    dic[l1[j]]=l2[j]
    j+=1
print(dic)