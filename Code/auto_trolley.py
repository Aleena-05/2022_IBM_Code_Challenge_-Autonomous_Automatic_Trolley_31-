import pandas as pd
import sys
import time
#class to mimic the junction
jlist=[]
#function to traceback path
def goback(x,junc):
    print("Final delivery done and the dispenser takes an aboutturn")
    time.sleep(2)
    if(x[-1]=='r'):
        print ("The medicine dispenser takes a left turn at junction ",jlist[junc].name)
        time.sleep(2)
    elif(x[-1]=='l'):
        print ("The medicine dispenser takes a right turn at junction ",jlist[junc].name)
        time.sleep(2)
    else:
        print ("Error")
        sys.exit()
    for i in range(index-1,-1,-1):
        print ("The medicine dispenser proceeds to junction ",jlist[i].name)
        time.sleep(2)
        print ("The medicine dispenser has reached junction ",jlist[i].name)
        time.sleep(2)
    print("The medicine dispenser reaches the initial position")
    time.sleep(2)
    sys.exit()
#class to mimic the junction        
class Junction:
    def __init__(self,name,right,left,fwd):
        self.name = name
        self.right = right
        self.left = left
        self.fwd = fwd
#reading junction details from csv file
df = pd.read_csv("rdetails.csv")
jnames=df.jname.tolist()
#creating array of objects
for i in range(0,len(jnames),1):
    jlist.append(Junction(df.jname[i],df.right[i],df.left[i],df.fwd[i]))
dq = []
rno=input("\nEnter room numbers:")
r=rno.split()
r=[int(i) for i in r]
r.sort()
print("The medicine dispenser is at the initial position")
time.sleep(2)
print("Fill medicine")
time.sleep(2)
rind=-1
#movements
for k in r:
    rind+=1
    index=-1
    dq.clear()
    print("Medicine dispenser aiming at room no ", k)
    time.sleep(2)
    print("The medicine dispenser proceeds to next junction")
    time.sleep(2)
    for i in jlist:
        index+=1
        print("Junction ",i.name," reached")
        time.sleep(2)
        #if the room to reach is towards the right of junction
        if (i.right==k):
            dq.append('r')
            print("Right Turn taken at ",i.name)
            time.sleep(2)
            print("Medicine Delivered")
            time.sleep(2)
            if(k==r[-1]):
                goback(dq,index)
                break
            else:
                print("About Turn taken\nThe medicine dispenser takes a right turn at junction", i.name)
                time.sleep(2)
                rind+=1
                k=r[rind]
                if(k==i.left):
                    print("Medicine dispenser aiming at room no ", k)
                    time.sleep(2)
                    print("The medicine dispenser takes a left turn at junction",i.name,)
                    time.sleep(2)
                    print("Medicine Delivered")
                    time.sleep(2)
                    if(k==r[-1]):
                        goback(dq,index)
                        break
                    else:
                         print("About Turn taken\nThe medicine dispenser takes a left turn at junction", i.name)
                         time.sleep(2)
                         rind+=1
                         k=r[rind]
                print("Medicine dispenser aiming at room no ", k)
                time.sleep(1)
                continue
        #if the room to reach is towards the left of junction
        elif (i.left==k):
            dq.append('l')
            print("Left Turn taken at",i.name)
            time.sleep(2)
            print("Medicine Delivered")
            time.sleep(2)
            if(k==r[-1]):
                goback(dq,index)
                break
            else:
                print("About Turn taken\nThe medicine dispenser takes a left turn at junction", i.name)
                time.sleep(2)
                rind+=1
                k=r[rind]
                if(k==i.right):
                    print("Medicine dispenser aiming at room no ", k)
                    time.sleep(2)
                    print("The medicine dispenser takes a right turn at junction",i.name)
                    time.sleep(2)
                    print("Medicine Delivered")
                    time.sleep(2)
                    if(k==r[-1]):
                        goback(dq,index)
                        break
                    else:
                         print("About Turn taken\nThe medicine dispenser takes a right turn at junction", i.name)
                         time.sleep(2)
                         rind+=1
                         k=r[rind]
                print("Medicine dispenser aiming at room no ", k)
                time.sleep(2)
                continue
        #when no more path is available
        elif(i.fwd==False):
            print("Room not found\nMedicine not delivered\nMedicine dispenser returns to initial position")
            sys.exit()
        #if the room to reach is not in the current junction
        else:
            print("The medicine dispenser proceeds to ",jlist[index+1].name,"junction")
            time.sleep(2)
