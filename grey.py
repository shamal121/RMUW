import numpy as np
import cv2
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

cap = cv2.VideoCapture(0)
x = 0
y = 0
X = 0
Y = 0
i = 0
count = 34*280

while(True):
    ser.readline()
    ret, frame = cap.read()
    X = 0
    Y = 0
    if i < 4:
        i+=1
    else:
	for X in range(100, 380):
	    for Y in range(150, 490):
	        g = frame.item(X,Y,0)
		b = frame.item(X,Y,1)
		r = frame.item(X,Y,2)     
		if r > 140 and b < 100 and g < 100:
		    x = Y + x
		    y = X + y 
        x = x/count
        y = y/count
	i = 0
	ser.write(x)
	#cv2.imshow('frame',frame)
	#if cv2.waitKey(1) & 0xFF == ord('q'):
	#    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
