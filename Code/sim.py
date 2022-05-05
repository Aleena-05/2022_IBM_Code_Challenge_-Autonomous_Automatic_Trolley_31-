#class to mimic the junction
def goback(x):
    l=len(x)
    for i in range(l-1,0,-1):
        if(x[i]=='f'):
            print("\nTrolley moves straight")
        elif(x[i]=='r'):
            print("\nTrolley moves left")
        elif(x[i]=='l'):
            print("\nTrolley moves right")
        else:
            print("\nTrolley moves backwards")
class Junction:
    def __init__(self,name,right,left,fwd):
        self.name = name
        self.right = right
        self.left = left
        self.fwd = fwd
flag=0
list=[]
#creating objects for each class
j1=Junction("J1",1,2,True)
j2=Junction("J2",3,4,True)
j3=Junction("J3",5,6,True)
j4=Junction("J4",7,8,False)
list.append(j1)
list.append(j2)
list.append(j3)
list.append(j4)
#stack to store the path
dq=[]
#Target room numbers input from the user
rno=input("\nEnter room numbers:")
r=rno.split()
r=[int(i) for i in r]
#motor movements
for k in r:
    dq.clear()
    print("\nTrolley in starting position\nFill medicine")
    print("\nTrolley moving to room no ",k)
    print("\nTrolley moves straight")
    dq.append('f')
    for i in list:
        dq.append('f')
        print("\nJunction ",i.name," reached")
        if (i.right==k):
            flag=1
            dq.append('r')
            print("\nRight Turn taken\nMedicine delivered\nAbout Turn\nTrolley moves straight")
            goback(dq)
            break
        elif (i.left==k):
            flag=1
            dq.append('l')
            print("\nLeft Turn taken\nMedicine delivered\nAbout Turn\nTrolley moves straight")
            goback(dq)
            break
        elif(i.fwd==False):
            dq.append('f')
            print("\nRoom not found\nMedicine not delivered\nAbout Turn")
            goback(dq)
            break
        else:
            print("\nTrolley moves straight")
            
            
