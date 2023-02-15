import numpy as np
import cv2
import binascii
from datetime import datetime, timedelta

# Import the video, and assign the sizes
videoPath = cv2.VideoCapture("blinkenlights-2.mp4")
width = videoPath.get(cv2.CAP_PROP_FRAME_WIDTH)
height = videoPath.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps =  videoPath.get(cv2.CAP_PROP_FPS)
bitString1 = ""
bitString2 = ""
red_center_old = 0
green_center_old = 0
firstTime = True
second = timedelta(0,1)
string1 = False
string2 = False
bit = "0"
testValue = ""
i = 0

# Set the width and height
videoPath.set(cv2.CAP_PROP_FRAME_WIDTH, width)
videoPath.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Set the position of the red light
red_x = 180
red_y = 740

# Set the position of the green light
green_x = 200
green_y = 740

print("Analyzing video...")
start_time = datetime.now()
end_time = datetime.now()
while True:
    ret, frame = videoPath.read()
    
    # Change the colors of the video
    if ret:
        # Turn window black/grey/white
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        # Seperate the black from the white
        thresholdValue = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)[1]
        # Seperate the black from the white
        
        # Make circles around the red and green dots
        cv2.circle(thresholdValue, (red_x,red_y),7,(255,0,0),1)
        cv2.circle(thresholdValue, (green_x,green_y),4,(255,0,0),1)
        
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(thresholdValue, str(datetime.now()), (50, 100), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        # Make video and show the results in a window
        cv2.imshow("Challenge 3 Video", thresholdValue)
    else:
        break
    
    # Define circle centers
    red_center_new = thresholdValue[red_y, red_x]
    green_center_new = thresholdValue[green_y, green_x]
    
    while ((red_center_new != red_center_old) or (green_center_new != green_center_old)):
    
        if (firstTime != True):
            end_time = start_time
            start_time = datetime.now()
            difference = start_time - end_time
            
            if (difference > second):
                if (red_center_old == 0 and green_center_old==255):
                    testValue = "String 1: "
                    bitString2 = bitString2[:-2]
                    string1 = True
                    string2 = False
                elif (red_center_old == 255 and green_center_old==0):
                    testValue = "String 2: "
                    bitString1 = bitString1[:-2]
                    string1 = False
                    string2 = True
                    
                    
            red_center_old = red_center_new
            green_center_old = green_center_new

            if ((string1 == True) and (string2 == False)):
                if ((red_center_new == 255) and (green_center_new == 255)):
                    bit = "1"
                elif ((red_center_new == 0) and (green_center_new == 0)):
                    bit = "0"
                elif ((red_center_new == 0) and (green_center_new == 255)):
                    bit = ""

                i = i+1
                bitString1 += bit
            else:
                if ((red_center_new == 255) and (green_center_new == 255)):
                    bit = "1"
                elif ((red_center_new == 0) and (green_center_new == 0)):
                    bit = "0"
                elif ((red_center_new == 255) and (green_center_new == 0)):
                    bit = ""
                
                bitString2 += bit
        else:
            firstTime = False
            end_time = start_time
            start_time = datetime.now()
            bit = ""
    # Push q to stop the script
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
videoPath.release()
cv2.destroyAllWindows()

bitString2 = bitString2[:-1]

xor_string = bin(int(bitString1,2) ^ int(bitString2,2))

xorInt = int(xor_string, 2)
answer = xorInt.to_bytes((xorInt.bit_length() + 7) // 8, 'big').decode()
print(answer)
