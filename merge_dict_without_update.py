s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
list=[s,a]
dic={}
i=0
while i<len(list):
    for j in list[i]:
        dic[j]=list[i][j]
    i=i+1
        
print(dic)