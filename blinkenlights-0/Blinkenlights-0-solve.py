import numpy as np
import cv2
import binascii

# Import the video, and assign the sizes
videoPath = cv2.VideoCapture("blinkenlights-0.mp4")
width = videoPath.get(cv2.CAP_PROP_FRAME_WIDTH)
height = videoPath.get(cv2.CAP_PROP_FRAME_HEIGHT)
bitString = ""
red_center_old = 0
green_center_old = 0

# Set the width and height
videoPath.set(cv2.CAP_PROP_FRAME_WIDTH, width)
videoPath.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Set the position of the red light
red_x = 232
red_y = 551

# Set the position of the green light
green_x = 250
green_y = 551

print("Analyzing video...")
while True:
    ret, frame = videoPath.read()
    
    # Change the colors of the video
    if ret:
        # Turn window black/grey/white
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        # Seperate the black from the white
        thresholdValue = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)[1]

        # Make circles around the red and green dots
        cv2.circle(thresholdValue, (red_x,red_y),4,(255,0,0),1)
        cv2.circle(thresholdValue, (green_x,green_y),4,(255,0,0),1)
        
        # Make video and show the results in a window
        cv2.imshow("Challenge 1 Video", thresholdValue)
    else:
        break

    # Define circle centers
    red_center_new = thresholdValue[red_y, red_x]
    green_center_new = thresholdValue[green_y, green_x]
    
    while ((red_center_new != red_center_old) or (green_center_new != green_center_old)):
        red_center_old = red_center_new
        green_center_old = green_center_new
        
        if ((red_center_new == 255) and (green_center_new != 255)):
            bitString += "1"
        elif ((red_center_new != 255) and (green_center_new == 255)):
            bitString += "0"
    # Push q to stop the script
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

videoPath.release()
cv2.destroyAllWindows()

xorInt = int(bitString, 2)
answer = xorInt.to_bytes((xorInt.bit_length() + 7) // 8, 'big').decode()
print(answer)
