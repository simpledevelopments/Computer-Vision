# Sample Code Snippet using NonBlockingVideoCapture with 2 cameras. Replace the IDs accordingly.
# You can want to throttle the loop, since it will loop very quickly due to "non blocking" reads.

from NonBlockingVideoCapture import NonBlockingVideoCapture
import numpy as np
import cv2
import time

print("Initializing 0..")
video_capture_0 = NonBlockingVideoCapture(src=0)
print("Initializing 1..")
video_capture_1 = NonBlockingVideoCapture(src=1)
print("All Initialized. Let's Go!")

while True: 
    ret0, frame0 = video_capture_0.read()
    ret1, frame1 = video_capture_1.read()

    if ret0 == False:
        print("Error reading from video capture 0")
        break
    elif ret1 == False:
        print("Error reading from video capture 1")
        break
    else:
        cv2.imshow('Cam 0 and 1', np.hstack([frame0,frame1]))
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()
print("Goodbye")
