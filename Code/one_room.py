#this code accomplishes the task of moving to one room. The user needs to input the room number that the medicine is to be delivered.
#the trolley starts moving and scans for qr code which is present at junctions. if the corresponding junction is reached the trolley turns into the room and delivers medicine
#the program prints the movements of the trolley accordingly
import sys
import cv2
import numpy as np
from pyzbar.pyzbar import decode
rno=int(input("Enter room number:"))
dq=[]
#function to traceback the movements to initial position
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
#function to print the motor actions to reach the room
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
#videocapture from webcam
cap = cv2.VideoCapture(0)

while True:
    success, img= cap.read()

    if not success:
        break
    #decoding qrcode
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
