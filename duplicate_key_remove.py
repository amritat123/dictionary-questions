dic1={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
for keys in dic1.items():
     print(dic1)

#second method..
i=0
while i<len (dic1):
    if i in dic1.items():
        i+=1
    print(dic1)
    break


