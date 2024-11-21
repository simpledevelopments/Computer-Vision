# NonBlockingVideoCapture
# 
# Use a separate thread to read from each camera, then each 
# non-blocking read simply takes the latest frame from that thread
#
# Usage:
#  Instead of : cam0 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#               (ret, frame) = cam0.read()  # Blocking
#               cam0.release()
#
#  You can use: cam0 = NonBlockingVideoCapture(0)
#               (ret, frame) = cam0.read()  # Non Blocking
#               cam0.release()              # Waits for thread to exit

from threading import Thread
import cv2

class NonBlockingVideoCapture:
    def __init__(self, src=0):
        """ 
        Initialize the camera stream, read the first frame, start thread
        """
        self.src = src
        self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.backgroundthread = Thread(target=self.update, args=())
        self.backgroundthread.start()
        
    def update(self):
        """ 
        Keep reading camera frames until the thread is stopped/released
        You can calculate camera FPS inside here, if needed
        """
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()
            
    def read(self):
        """
        Return the most recent frame read
        """
        if self.grabbed == True and self.frame is not None and self.stopped == False:
            return (self.grabbed, self.frame.copy())
        else:
            return (False, None)
            
    def release(self):  
        """
        Stop the thread, release the camera
        """
        self.stopped = True    
        self.backgroundthread.join()
        self.stream.release()
        
        # print(str(self.src)+" released")
