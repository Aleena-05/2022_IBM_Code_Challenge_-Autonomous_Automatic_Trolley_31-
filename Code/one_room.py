import sys
import cv2
import numpy as np
from pyzbar.pyzbar import decode
rno=int(input("Enter room number:"))
dq=[]
def moveback(x):
    print("Trolley takes aboutturn")
    for i in x:
        if(i=='f'):
            print("Trolley moves straight")
        elif(i=='r'):
            print("Trolley moves left")
        elif(i=='l'):
            print("Trolley moves right")
        else:
            print("Wrong")
    print("Trolley has reached initial position")
    sys.exit()
def mov(m):
    a=m.split()
    a=[int(i) for i in a]
    if(rno in a):
        if(a[0]==rno):
            dq.append('r')
            dq.append('f')
            print("Trolley takes a right\nTrolley moves straight\nGives medicine")
            moveback(dq)
        else:
            dq.append('l')
            dq.append('f')
            print("Trolley takes a left\nTrolley moves straight\nGives medicine")
            moveback(dq)
    else:
        print("Trolley proceeds to next junction")

cap = cv2.VideoCapture(0)

while True:
    success, img= cap.read()

    if not success:
        break
    for code in decode(img):
        #print(code.data.decode("utf-8"))
        myData=code.data.decode("utf-8")
        if(myData):
            print("Junction reached")
            dq.clear()
            dq.append('f')
            mov(myData)

    cv2.imshow("image",img)
    cv2.waitKey(1)

cap.release()
cap.destroywindow()
