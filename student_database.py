student_db={}
#ask input from user or "q" to exit..
while True:
    user=input("please enter the id and name saprete with couma or q to exit=")
    if user=="q":
        break
    id,name=user.split(",")
    student_db.update({id:name})
    #output
    for x,y in student_db.items():
        print(x,y)
    #serching a key
    key=input("enter the id to serach")
    if key in student_db:
        print('key=',key,'value=',student_db[key])
    else:
        print("key not found")

