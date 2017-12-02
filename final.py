from Functions import *
import cv2
import time
import easygopigo3 as easy
gpg=easy.EasyGoPiGo3()


def interpreter():
    gpg.set_eye_color((255,255,255))
    index=3
    dest=0
    while dest==0:
        ans=numDots('filePath') #placeholder, it'll have to be taken in from the camera
        if ans==1:
            gpg.open_left_eye()
            time.sleep(.5)
            gpg.close_left_eye()
            gpg.turn_degrees(-90,True)
            gpg.drive_inches(12,True)
            gpg.turn_degrees(90,True)
            index-=1
        elif ans==2:
            open_right_eye()
            time.sleep(.5)
            close_right_eye()
            gpg.turn_degrees(-90,True)
            gpg.drive_inches(12,True)
            gpg.turn_degrees(90,True)
            index+=1
        else:
            dest=True
            gpg.set_eye_color((255,0,0))
            for i in index:
                gpg.open_left_eye()
                gpg.time.sleep(.5)
                gpg.close_left_eye()
            gpg.set_eye_color((0,0,255))
            for i in ans:
                gpg.open_left_eye()
                gpg.time.sleep(.5)
                gpg.close_left_eye()
            return ans