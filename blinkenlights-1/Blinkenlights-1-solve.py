import numpy as np
import cv2
import binascii
import time

# Import the video, and assign the sizes
videoPath = cv2.VideoCapture("blinkenlights-1.mp4")
width = videoPath.get(cv2.CAP_PROP_FRAME_WIDTH)
height = videoPath.get(cv2.CAP_PROP_FRAME_HEIGHT)
bit = True
spaceSwitch = True
bitString = ""
i = 0

# Set the width and height
videoPath.set(cv2.CAP_PROP_FRAME_WIDTH, width)
videoPath.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Set the position of the red light
red_x = 208
red_y = 551

# Set the position of the green light
green_x = 224
green_y = 550

print("Analyzing video...")
while True:
    ret, frame = videoPath.read()
    # Change the colors of the video
    if ret:
        # Turn window black/grey/white
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        # Seperate the black from the white
        thresholdValue = cv2.threshold(blurred, 205, 255, cv2.THRESH_BINARY)[1]
        
        # Make circles around the red and green dots
        cv2.circle(thresholdValue, (red_x,red_y),8,(255,0,0),1)
        cv2.circle(thresholdValue, (green_x,green_y),5,(255,0,0),1)
        # Make video and show the results in a window
        cv2.imshow("Challenge 2 Video", thresholdValue)
    else:
        break

    # Define circle centers
    red_center = thresholdValue[red_y, red_x]
    green_center = thresholdValue[green_y, green_x]
    
    # If the red light is on, but not the green, bit is .
    if red_center == 255 and green_center != 255 and bit==True:
        bitString += "."
        bit = False
        spaceSwitch = True
        i = i + 1
    
    # If the green and red lights are on, bit is -
    elif red_center == 255 and green_center == 255 and bit==True:
        bitString += "-"
        bit = False
        spaceSwitch = True
        i = i + 1
    
    # If the green and red lights are both off, do nothing
    elif red_center == 0 and green_center == 0 and bit==False:
        bit = True
    
    # Add spaces at pauses
    if (i==2 or i==7 or i==10 or i==11 or i==14 or i==19 or i==23 or i==26 or i==31 or i==36 or i==41 or i==46 or i==51 or i==56 or i==61) and spaceSwitch==True:
        bitString += " "
        spaceSwitch = False
    
    # Push q to stop the script
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

videoPath.release()
cv2.destroyAllWindows()

# Print string to decode
print(bitString)
