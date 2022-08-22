import os
def write_Info():
    f=open("data.txt","a")
    s=input("enter empId,name,salary,designation : ")
    f.write(s+"\n")
    f.close()


def delete():
    f=open("data.txt","r+")
    t=open("temp.txt","a")
    if os.path.getsize("data.txt") == 0:
        print("file is empty.......")
    else:
        s=input("Enter empId to delete: ")
        for line in f.readlines():
            if s not in line:
                t.write(line)
    f.close()
    t.close()
    os.replace("temp.txt","data.txt")
    display()
    
            
def update():
    f=open("data.txt","r+")
    t=open("update.txt","r+")
    if os.path.getsize("data.txt") == 0:
        print("file is empty")
    else:
        r=input("enter empId :")
        for line in f.readlines():
            l=line.split(",")
            if r==l[0]:
                n=int(input("enter the parameter to update(1.name/2.salary/3.designation/4.experience):"))
                if(n==1):
                    name=input("enter employee name to update :")
                    l[1]=name
                elif(n==2):
                    salary=input("enter salary to update:")
                    l[2]=salary
                elif(n==3):
                    designation=input("Enter designation to update: ")
                    l[3]=designation
                s=','.join(l)
                t.write(s)
            else:
                t.write(line)

        
    f.close()
    t.close()
    os.replace("update.txt","data.txt")
    display()
def display():
    f=open("data.txt","r")
    if os.path.getsize("data.txt") == 0:
        print("file is empty......")
    else:
        d=input("1.display all data\n2.display particular data\n")
        if(d=="1"):
            for line in f.readlines():
                print(line)
        elif(d=='2'):
            print("particular employee information\n")
            p=input("enter empId: ")
            for line in f.readlines():
                if p in line:
                    print(line)
    f.close()            
def search():
    if os.path.getsize("data.txt") == 0:
        print("file is empty.......")
    else:
        search=input("enter empId to search: ")
        f=open("data.txt","r+")
        for line in f.readlines():
            if search in line:
                print("details found.....")
                print(line)
            else:
                print("details not found")
        f.close()
            
    
    
while True:
    print("1.write\n2.delete\n3.update\n4.display\n5.search\n")
    a=input("enter your option:")
    if(a=="1"):
        write_Info()
    elif(a=="2"):
        delete()
    elif(a=="3"):
        update()
    elif(a=="4"):
        display()
    elif(a=="5"):
        search()
    print("u want to perform more operation(y/n):")
    ch=input("enter y or n:")
    if(ch=="n" or ch=="N"):
        break
        



